from allauth.socialaccount.models import SocialAccount
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.contrib.auth.models import User
from django.core.exceptions import PermissionDenied
from django.db.models import Exists, OuterRef, Q
from django.shortcuts import get_object_or_404, render
from django.views.decorators.http import require_http_methods
from django.views.generic.base import TemplateView
from django_filters.views import FilterView

from dandiapi.api.filters import UserStatusFilter
from dandiapi.api.mail import send_approved_user_message, send_rejected_user_message
from dandiapi.api.models import Asset, AssetBlob, Upload, UserMetadata, Version
from dandiapi.api.views.users import social_account_to_dict


class DashboardMixin(LoginRequiredMixin, UserPassesTestMixin):
    def test_func(self):
        return self.request.user.is_superuser


class DashboardView(DashboardMixin, TemplateView):
    template_name = 'dashboard/index.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['orphaned_asset_count'] = self._orphaned_asset_count()
        context['orphaned_asset_blob_count'] = self._orphaned_asset_blob_count()
        non_valid_assets = self._non_valid_assets()
        context['non_valid_asset_count'] = non_valid_assets.count()
        context['non_valid_assets'] = non_valid_assets[:10]
        uploads = self._uploads()
        context['upload_count'] = uploads.count()
        context['uploads'] = uploads[:10]
        users = self._users()
        context['user_count'] = users.count()
        context['users'] = users

        return context

    def _orphaned_asset_count(self):
        return (
            Asset.objects.annotate(
                has_version=Exists(Version.objects.filter(assets=OuterRef('id')))
            )
            .filter(has_version=False)
            .count()
        )

    def _orphaned_asset_blob_count(self):
        return (
            AssetBlob.objects.annotate(
                has_asset=Exists(Asset.objects.filter(blob_id=OuterRef('id')))
            )
            .filter(has_asset=False)
            .count()
        )

    def _non_valid_assets(self):
        return (
            Asset.objects.annotate(
                has_version=Exists(Version.objects.filter(assets=OuterRef('id')))
            )
            .filter(has_version=True)
            .filter(~Q(status=Asset.Status.VALID))
        )

    def _uploads(self):
        return Upload.objects.annotate()

    def _users(self):
        return (
            User.objects.select_related('metadata')
            .filter(metadata__status=UserMetadata.Status.APPROVED)
            .order_by('-date_joined')
        )


class UserDashboardView(DashboardMixin, FilterView):
    template_name = 'dashboard/users.html'
    filterset_class = UserStatusFilter
    queryset = User.objects.filter(~Q(username='AnonymousUser')).order_by('date_joined')


@require_http_methods(['GET', 'POST'])
def user_approval_view(request, username: str):
    if not request.user.is_superuser:
        raise PermissionDenied()

    user: User = get_object_or_404(User.objects.select_related('metadata'), username=username)
    social_account: SocialAccount = user.socialaccount_set.first()

    if request.method == 'POST':
        req_body = request.POST.dict()
        user.metadata.status = req_body.get('status')
        if req_body.get('rejection_reason') is not None:
            user.metadata.rejection_reason = req_body.get('rejection_reason')
        user.metadata.save()

        if user.metadata.status == UserMetadata.Status.APPROVED:
            send_approved_user_message(user, social_account)
        elif user.metadata.status == UserMetadata.Status.REJECTED:
            send_rejected_user_message(user, social_account)
            user.is_active = False
            user.save()

    return render(
        request,
        'dashboard/user_approval.html',
        {
            'user': user,
            'social_account': social_account_to_dict(social_account)
            if social_account is not None
            else None,
        },
    )
