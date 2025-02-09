# v0.3.18 (Wed Feb 22 2023)

#### 🐛 Bug Fix

- Release with auto [#1500](https://github.com/dandi/dandi-archive/pull/1500) ([@AlmightyYakob](https://github.com/AlmightyYakob))
- Rename field in zarr file request to `base64md5` for clarity [#1498](https://github.com/dandi/dandi-archive/pull/1498) ([@AlmightyYakob](https://github.com/AlmightyYakob))
- Add back md5 to zarr object url signing [#1497](https://github.com/dandi/dandi-archive/pull/1497) ([@danlamanna](https://github.com/danlamanna) [@AlmightyYakob](https://github.com/AlmightyYakob))
- Remove overly aggressive exception handling [#1490](https://github.com/dandi/dandi-archive/pull/1490) ([@danlamanna](https://github.com/danlamanna))

#### 🏠 Internal

- Bump types-setuptools from 67.2.0.1 to 67.3.0.1 [#1495](https://github.com/dandi/dandi-archive/pull/1495) ([@dependabot[bot]](https://github.com/dependabot[bot]))
- Pin to Node 16 in CI [#1496](https://github.com/dandi/dandi-archive/pull/1496) ([@mvandenburgh](https://github.com/mvandenburgh))

#### Authors: 4

- [@dependabot[bot]](https://github.com/dependabot[bot])
- Dan LaManna ([@danlamanna](https://github.com/danlamanna))
- Jacob Nesbitt ([@AlmightyYakob](https://github.com/AlmightyYakob))
- Mike VanDenburgh ([@mvandenburgh](https://github.com/mvandenburgh))

---

# v0.3.17 (Tue Feb 21 2023)

#### 🐛 Bug Fix

- Display error message for invalid dandiset URL [#1454](https://github.com/dandi/dandi-archive/pull/1454) ([@mvandenburgh](https://github.com/mvandenburgh))

#### Authors: 1

- Mike VanDenburgh ([@mvandenburgh](https://github.com/mvandenburgh))

---

# v0.3.16 (Thu Feb 16 2023)

#### 🐛 Bug Fix

- Add locking to asset update/delete at API level [#1485](https://github.com/dandi/dandi-archive/pull/1485) ([@AlmightyYakob](https://github.com/AlmightyYakob))
- Convert `OverviewTab` component to `<script setup>` [#1453](https://github.com/dandi/dandi-archive/pull/1453) ([@mvandenburgh](https://github.com/mvandenburgh))
- Stop trimming characters off of test zarr paths [#1493](https://github.com/dandi/dandi-archive/pull/1493) ([@danlamanna](https://github.com/danlamanna))

#### 🏠 Internal

- Bump flake8-bugbear from 23.1.20 to 23.2.13 [#1492](https://github.com/dandi/dandi-archive/pull/1492) ([@dependabot[bot]](https://github.com/dependabot[bot]))
- Bump types-setuptools from 67.1.0.0 to 67.2.0.1 [#1491](https://github.com/dandi/dandi-archive/pull/1491) ([@dependabot[bot]](https://github.com/dependabot[bot]))

#### Authors: 4

- [@dependabot[bot]](https://github.com/dependabot[bot])
- Dan LaManna ([@danlamanna](https://github.com/danlamanna))
- Jacob Nesbitt ([@AlmightyYakob](https://github.com/AlmightyYakob))
- Mike VanDenburgh ([@mvandenburgh](https://github.com/mvandenburgh))

---

# v0.3.15 (Mon Feb 13 2023)

#### 🐛 Bug Fix

- Skip computing assets summary for invalid assets [#1489](https://github.com/dandi/dandi-archive/pull/1489) ([@danlamanna](https://github.com/danlamanna))

#### Authors: 1

- Dan LaManna ([@danlamanna](https://github.com/danlamanna))

---

# v0.3.14 (Fri Feb 10 2023)

#### 🐛 Bug Fix

- Implement new zarr upload process [#1448](https://github.com/dandi/dandi-archive/pull/1448) ([@AlmightyYakob](https://github.com/AlmightyYakob))
- Simplify zarr upload process design [#1464](https://github.com/dandi/dandi-archive/pull/1464) ([@AlmightyYakob](https://github.com/AlmightyYakob))
- Upgrade black to 23.1.0 [#1465](https://github.com/dandi/dandi-archive/pull/1465) ([@AlmightyYakob](https://github.com/AlmightyYakob))
- Restore published version emulation for validation purposes [#1459](https://github.com/dandi/dandi-archive/pull/1459) ([@danlamanna](https://github.com/danlamanna))
- Update DLP UI for asynchronous assets summary [#1452](https://github.com/dandi/dandi-archive/pull/1452) ([@mvandenburgh](https://github.com/mvandenburgh))
- Compute asset summary asynchronously for draft versions [#1431](https://github.com/dandi/dandi-archive/pull/1431) ([@danlamanna](https://github.com/danlamanna))

#### 🏠 Internal

- Bump types-setuptools from 65.7.0.1 to 67.1.0.0 [#1467](https://github.com/dandi/dandi-archive/pull/1467) ([@dependabot[bot]](https://github.com/dependabot[bot]))
- Bump mypy from 0.991 to 1.0.0 [#1468](https://github.com/dandi/dandi-archive/pull/1468) ([@dependabot[bot]](https://github.com/dependabot[bot]))
- Bump flake8-docstrings from 1.6.0 to 1.7.0 [#1458](https://github.com/dandi/dandi-archive/pull/1458) ([@dependabot[bot]](https://github.com/dependabot[bot]))
- Bump django-stubs from 1.13.1 to 1.14.0 [#1457](https://github.com/dandi/dandi-archive/pull/1457) ([@dependabot[bot]](https://github.com/dependabot[bot]))

#### Authors: 4

- [@dependabot[bot]](https://github.com/dependabot[bot])
- Dan LaManna ([@danlamanna](https://github.com/danlamanna))
- Jacob Nesbitt ([@AlmightyYakob](https://github.com/AlmightyYakob))
- Mike VanDenburgh ([@mvandenburgh](https://github.com/mvandenburgh))

---

# v0.3.13 (Fri Jan 27 2023)

#### 🐛 Bug Fix

- Add 12 hour cache to stats endpoint [#1416](https://github.com/dandi/dandi-archive/pull/1416) ([@AlmightyYakob](https://github.com/AlmightyYakob))

#### 🏠 Internal

- Bump flake8-bugbear from 22.12.6 to 23.1.20 [#1446](https://github.com/dandi/dandi-archive/pull/1446) ([@dependabot[bot]](https://github.com/dependabot[bot]))

#### Authors: 2

- [@dependabot[bot]](https://github.com/dependabot[bot])
- Jacob Nesbitt ([@AlmightyYakob](https://github.com/AlmightyYakob))

---

# v0.3.12 (Mon Jan 23 2023)

#### 🐛 Bug Fix

- Require rejection reason when rejecting a new user [#1443](https://github.com/dandi/dandi-archive/pull/1443) ([@mvandenburgh](https://github.com/mvandenburgh))
- Fix dependabot ignore types [#1445](https://github.com/dandi/dandi-archive/pull/1445) ([@danlamanna](https://github.com/danlamanna))

#### Authors: 2

- Dan LaManna ([@danlamanna](https://github.com/danlamanna))
- Mike VanDenburgh ([@mvandenburgh](https://github.com/mvandenburgh))

---

# v0.3.11 (Mon Jan 23 2023)

#### 🐛 Bug Fix

- Fix publishing UI bug [#1442](https://github.com/dandi/dandi-archive/pull/1442) ([@mvandenburgh](https://github.com/mvandenburgh))
- Allow deleting embargoed dandisets [#1438](https://github.com/dandi/dandi-archive/pull/1438) ([@danlamanna](https://github.com/danlamanna))
- ENH: explicitly describe both cases of not allowed dandiset deletion [#1433](https://github.com/dandi/dandi-archive/pull/1433) ([@yarikoptic](https://github.com/yarikoptic))
- Fix dependabot ignore type [#1437](https://github.com/dandi/dandi-archive/pull/1437) ([@danlamanna](https://github.com/danlamanna))
- Add design doc for Zarr upload process simplification [#1415](https://github.com/dandi/dandi-archive/pull/1415) ([@waxlamp](https://github.com/waxlamp) [@AlmightyYakob](https://github.com/AlmightyYakob))

#### 🏠 Internal

- Bump types-setuptools from 65.6.0.3 to 65.7.0.1 [#1434](https://github.com/dandi/dandi-archive/pull/1434) ([@dependabot[bot]](https://github.com/dependabot[bot]))
- Bump boto3-stubs[s3] from 1.26.46 to 1.26.50 [#1435](https://github.com/dandi/dandi-archive/pull/1435) ([@dependabot[bot]](https://github.com/dependabot[bot]))

#### Authors: 6

- [@dependabot[bot]](https://github.com/dependabot[bot])
- Dan LaManna ([@danlamanna](https://github.com/danlamanna))
- Jacob Nesbitt ([@AlmightyYakob](https://github.com/AlmightyYakob))
- Mike VanDenburgh ([@mvandenburgh](https://github.com/mvandenburgh))
- Roni Choudhury ([@waxlamp](https://github.com/waxlamp))
- Yaroslav Halchenko ([@yarikoptic](https://github.com/yarikoptic))

---

# v0.3.10 (Wed Jan 11 2023)

#### 🐛 Bug Fix

- Remove use of checksum files in zarr ingestion [#1395](https://github.com/dandi/dandi-archive/pull/1395) ([@AlmightyYakob](https://github.com/AlmightyYakob))
- Add request timeouts for S3 storage [#1428](https://github.com/dandi/dandi-archive/pull/1428) ([@danlamanna](https://github.com/danlamanna))
- Add MINIO_STORAGE_MEDIA_URL to docker-compose-native config [#1427](https://github.com/dandi/dandi-archive/pull/1427) ([@danlamanna](https://github.com/danlamanna))

#### 🏠 Internal

- Bump boto3-stubs[s3] from 1.26.41 to 1.26.46 [#1429](https://github.com/dandi/dandi-archive/pull/1429) ([@dependabot[bot]](https://github.com/dependabot[bot]))
- Bump types-setuptools from 65.6.0.2 to 65.6.0.3 [#1430](https://github.com/dandi/dandi-archive/pull/1430) ([@dependabot[bot]](https://github.com/dependabot[bot]))

#### Authors: 3

- [@dependabot[bot]](https://github.com/dependabot[bot])
- Dan LaManna ([@danlamanna](https://github.com/danlamanna))
- Jacob Nesbitt ([@AlmightyYakob](https://github.com/AlmightyYakob))

---

# v0.3.9 (Mon Jan 09 2023)

#### 🐛 Bug Fix

- Reduce sentry performance sample rate for asset download [#1417](https://github.com/dandi/dandi-archive/pull/1417) ([@danlamanna](https://github.com/danlamanna))
- Ignore patch updates for dependabot [#1426](https://github.com/dandi/dandi-archive/pull/1426) ([@danlamanna](https://github.com/danlamanna))
- Add more detailed logging to development postgres [#1414](https://github.com/dandi/dandi-archive/pull/1414) ([@danlamanna](https://github.com/danlamanna))
- Remove redundant call to update_asset_paths [#1413](https://github.com/dandi/dandi-archive/pull/1413) ([@danlamanna](https://github.com/danlamanna))

#### 🏠 Internal

- Bump flake8-isort from 5.0.3 to 6.0.0 [#1419](https://github.com/dandi/dandi-archive/pull/1419) ([@dependabot[bot]](https://github.com/dependabot[bot]))
- Bump boto3-stubs[s3] from 1.26.32 to 1.26.41 [#1422](https://github.com/dandi/dandi-archive/pull/1422) ([@dependabot[bot]](https://github.com/dependabot[bot]))
- Bump flake8-black from 0.3.5 to 0.3.6 [#1420](https://github.com/dandi/dandi-archive/pull/1420) ([@dependabot[bot]](https://github.com/dependabot[bot]))
- Bump pep8-naming from 0.13.2 to 0.13.3 [#1410](https://github.com/dandi/dandi-archive/pull/1410) ([@dependabot[bot]](https://github.com/dependabot[bot]))

#### Authors: 2

- [@dependabot[bot]](https://github.com/dependabot[bot])
- Dan LaManna ([@danlamanna](https://github.com/danlamanna))

---

# v0.3.8 (Mon Dec 19 2022)

#### 🐛 Bug Fix

- Use flat file listing in zarr file browser [#1394](https://github.com/dandi/dandi-archive/pull/1394) ([@AlmightyYakob](https://github.com/AlmightyYakob))
- Use proper syntax for only locking ZarrArchive table [#1398](https://github.com/dandi/dandi-archive/pull/1398) ([@danlamanna](https://github.com/danlamanna))
- Simplify ingest_zarr_archive task [#1391](https://github.com/dandi/dandi-archive/pull/1391) ([@AlmightyYakob](https://github.com/AlmightyYakob))
- Batch bulk_create calls in publish [#1400](https://github.com/dandi/dandi-archive/pull/1400) ([@mvandenburgh](https://github.com/mvandenburgh))
- Remove special casing of backups2datalad user agent [#1397](https://github.com/dandi/dandi-archive/pull/1397) ([@danlamanna](https://github.com/danlamanna))
- Optimize `ingest_zarr_archive` task [#1387](https://github.com/dandi/dandi-archive/pull/1387) ([@AlmightyYakob](https://github.com/AlmightyYakob))

#### 🏠 Internal

- Bump flake8 from 5.0.4 to 6.0.0 [#1404](https://github.com/dandi/dandi-archive/pull/1404) ([@dependabot[bot]](https://github.com/dependabot[bot]))
- Bump flake8-quotes from 3.3.1 to 3.3.2 [#1409](https://github.com/dandi/dandi-archive/pull/1409) ([@dependabot[bot]](https://github.com/dependabot[bot]))
- Bump mypy from 0.982 to 0.991 [#1407](https://github.com/dandi/dandi-archive/pull/1407) ([@dependabot[bot]](https://github.com/dependabot[bot]))
- Bump boto3-stubs[s3] from 1.26.27 to 1.26.32 [#1405](https://github.com/dandi/dandi-archive/pull/1405) ([@dependabot[bot]](https://github.com/dependabot[bot]))
- Manage CI dependencies with dependabot [#1402](https://github.com/dandi/dandi-archive/pull/1402) ([@mvandenburgh](https://github.com/mvandenburgh))
- [gh-actions](deps): Bump actions/add-to-project from 0.3.0 to 0.4.0 [#1382](https://github.com/dandi/dandi-archive/pull/1382) ([@dependabot[bot]](https://github.com/dependabot[bot]))
- Move asset publishing to publish service [#1399](https://github.com/dandi/dandi-archive/pull/1399) ([@mvandenburgh](https://github.com/mvandenburgh))
- Specify `requests` as a prod dependency instead of test [#1401](https://github.com/dandi/dandi-archive/pull/1401) ([@mvandenburgh](https://github.com/mvandenburgh))
- Optimize memory use in publish service [#1376](https://github.com/dandi/dandi-archive/pull/1376) ([@mvandenburgh](https://github.com/mvandenburgh))
- Move metadata validation tasks into the service layer [#1379](https://github.com/dandi/dandi-archive/pull/1379) ([@mvandenburgh](https://github.com/mvandenburgh))

#### Authors: 4

- [@dependabot[bot]](https://github.com/dependabot[bot])
- Dan LaManna ([@danlamanna](https://github.com/danlamanna))
- Jacob Nesbitt ([@AlmightyYakob](https://github.com/AlmightyYakob))
- Mike VanDenburgh ([@mvandenburgh](https://github.com/mvandenburgh))

---

# v0.3.7 (Wed Dec 07 2022)

#### 🐛 Bug Fix

- Refresh asset object before validating it after creation [#1393](https://github.com/dandi/dandi-archive/pull/1393) ([@mvandenburgh](https://github.com/mvandenburgh))

#### Authors: 1

- Mike VanDenburgh ([@mvandenburgh](https://github.com/mvandenburgh))

---

# v0.3.6 (Tue Dec 06 2022)

#### 🐛 Bug Fix

- Always clear checksum files during zarr ingestion [#1390](https://github.com/dandi/dandi-archive/pull/1390) ([@AlmightyYakob](https://github.com/AlmightyYakob))

#### 📝 Documentation

- dandi-archive web app readme edit [#1386](https://github.com/dandi/dandi-archive/pull/1386) ([@melster1010](https://github.com/melster1010))

#### Authors: 2

- Jacob Nesbitt ([@AlmightyYakob](https://github.com/AlmightyYakob))
- Mary Elise Dedicke ([@melster1010](https://github.com/melster1010))

---

# v0.3.5 (Wed Nov 30 2022)

#### 🐛 Bug Fix

- Prevent locking dandisets during zarr upload [#1385](https://github.com/dandi/dandi-archive/pull/1385) ([@danlamanna](https://github.com/danlamanna))

#### Authors: 1

- Dan LaManna ([@danlamanna](https://github.com/danlamanna))

---

# v0.3.4 (Tue Nov 29 2022)

#### 🐛 Bug Fix

- Add file upload instructions to file browser UI [#1342](https://github.com/dandi/dandi-archive/pull/1342) ([@mvandenburgh](https://github.com/mvandenburgh))

#### 🏠 Internal

- Convert FileBrowser component to <script setup> [#1340](https://github.com/dandi/dandi-archive/pull/1340) ([@mvandenburgh](https://github.com/mvandenburgh))
- Convert `Meditor.vue` to `<script setup>` [#1303](https://github.com/dandi/dandi-archive/pull/1303) ([@mvandenburgh](https://github.com/mvandenburgh))

#### Authors: 1

- Mike VanDenburgh ([@mvandenburgh](https://github.com/mvandenburgh))

---

# v0.3.3 (Tue Nov 29 2022)

#### 🐛 Bug Fix

- Fix publishing being allowed for pending assets [#1383](https://github.com/dandi/dandi-archive/pull/1383) ([@mvandenburgh](https://github.com/mvandenburgh))
- Temporarily pin flake8 [#1380](https://github.com/dandi/dandi-archive/pull/1380) ([@mvandenburgh](https://github.com/mvandenburgh))

#### Authors: 1

- Mike VanDenburgh ([@mvandenburgh](https://github.com/mvandenburgh))

---

# v0.3.2 (Mon Nov 21 2022)

#### 🐛 Bug Fix

- Fix file browser bug [#1374](https://github.com/dandi/dandi-archive/pull/1374) ([@mvandenburgh](https://github.com/mvandenburgh))
- After Asset metadata validation, update Version timestamp with single query [#1373](https://github.com/dandi/dandi-archive/pull/1373) ([@mvandenburgh](https://github.com/mvandenburgh))
- Improved pagination design in file browser [#1311](https://github.com/dandi/dandi-archive/pull/1311) ([@mvandenburgh](https://github.com/mvandenburgh))
- add zarr validator service [#1370](https://github.com/dandi/dandi-archive/pull/1370) ([@satra](https://github.com/satra))
- Add embargo service [#1367](https://github.com/dandi/dandi-archive/pull/1367) ([@AlmightyYakob](https://github.com/AlmightyYakob))
- Properly handle conflicting asset paths [#1368](https://github.com/dandi/dandi-archive/pull/1368) ([@AlmightyYakob](https://github.com/AlmightyYakob))

#### 🏠 Internal

- Convert `DandisetLandingView` to `<script setup>`, use `vue-router` composable [#1316](https://github.com/dandi/dandi-archive/pull/1316) ([@mvandenburgh](https://github.com/mvandenburgh))
- Internal publishing service [#1363](https://github.com/dandi/dandi-archive/pull/1363) ([@mvandenburgh](https://github.com/mvandenburgh))

#### Authors: 3

- Jacob Nesbitt ([@AlmightyYakob](https://github.com/AlmightyYakob))
- Mike VanDenburgh ([@mvandenburgh](https://github.com/mvandenburgh))
- Satrajit Ghosh ([@satra](https://github.com/satra))

---

# v0.3.1 (Tue Nov 15 2022)

#### 🐛 Bug Fix

- Save draft versions during asset metadata validation [#1366](https://github.com/dandi/dandi-archive/pull/1366) ([@AlmightyYakob](https://github.com/AlmightyYakob))
- Refactor asset create/update/delete [#1352](https://github.com/dandi/dandi-archive/pull/1352) ([@danlamanna](https://github.com/danlamanna))
- Add YouTube channel to approved/registered emails [#1305](https://github.com/dandi/dandi-archive/pull/1305) ([@yarikoptic](https://github.com/yarikoptic))

#### 📝 Documentation

- dandi-archive readme edit [#1357](https://github.com/dandi/dandi-archive/pull/1357) ([@melster1010](https://github.com/melster1010))

#### 🧪 Tests

- Separate backend CI into separate jobs [#1360](https://github.com/dandi/dandi-archive/pull/1360) ([@mvandenburgh](https://github.com/mvandenburgh))
- Pin mypy [#1359](https://github.com/dandi/dandi-archive/pull/1359) ([@mvandenburgh](https://github.com/mvandenburgh))

#### Authors: 5

- Dan LaManna ([@danlamanna](https://github.com/danlamanna))
- Jacob Nesbitt ([@AlmightyYakob](https://github.com/AlmightyYakob))
- Mary Elise Dedicke ([@melster1010](https://github.com/melster1010))
- Mike VanDenburgh ([@mvandenburgh](https://github.com/mvandenburgh))
- Yaroslav Halchenko ([@yarikoptic](https://github.com/yarikoptic))

---

# v0.3.0 (Mon Nov 07 2022)

#### 🚀 Enhancement

- [gh-actions](deps): Bump actions/add-to-project from 0.0.3 to 0.3.0 [#1331](https://github.com/dandi/dandi-archive/pull/1331) ([@dependabot[bot]](https://github.com/dependabot[bot]))

#### 🐛 Bug Fix

- Add tqdm to asset path version ingestion [#1358](https://github.com/dandi/dandi-archive/pull/1358) ([@AlmightyYakob](https://github.com/AlmightyYakob))
- Fix oauth client error [#1354](https://github.com/dandi/dandi-archive/pull/1354) ([@mvandenburgh](https://github.com/mvandenburgh))
- Make asset paths operations idempotent [#1351](https://github.com/dandi/dandi-archive/pull/1351) ([@AlmightyYakob](https://github.com/AlmightyYakob))
- Delete unused management command import_dandisets.py [#1335](https://github.com/dandi/dandi-archive/pull/1335) ([@danlamanna](https://github.com/danlamanna))
- Optimize version/zarr asset path ingestion [#1343](https://github.com/dandi/dandi-archive/pull/1343) ([@AlmightyYakob](https://github.com/AlmightyYakob))
- Add Dandi exception classes [#1337](https://github.com/dandi/dandi-archive/pull/1337) ([@danlamanna](https://github.com/danlamanna))
- Disable APPROVE button if user is already approved [#1348](https://github.com/dandi/dandi-archive/pull/1348) ([@waxlamp](https://github.com/waxlamp))
- Fix dandiset deletion when containing zarrs [#1345](https://github.com/dandi/dandi-archive/pull/1345) ([@AlmightyYakob](https://github.com/AlmightyYakob))
- Fix asset update/deletion when associated with zarr [#1338](https://github.com/dandi/dandi-archive/pull/1338) ([@AlmightyYakob](https://github.com/AlmightyYakob))
- Optimize Asset Paths [#1312](https://github.com/dandi/dandi-archive/pull/1312) ([@AlmightyYakob](https://github.com/AlmightyYakob))
- Wait until after publish transaction commits to create DOI [#1330](https://github.com/dandi/dandi-archive/pull/1330) ([@mvandenburgh](https://github.com/mvandenburgh))
- Revert "[gh-actions](deps): Bump actions/add-to-project from 0.0.3 to 0.3.0" [#1327](https://github.com/dandi/dandi-archive/pull/1327) ([@mvandenburgh](https://github.com/mvandenburgh))
- Restore DLP loading bar, add skeleton loader [#1315](https://github.com/dandi/dandi-archive/pull/1315) ([@mvandenburgh](https://github.com/mvandenburgh))
- Remove vague TODO comment [#1288](https://github.com/dandi/dandi-archive/pull/1288) ([@danlamanna](https://github.com/danlamanna))
- Prevent deletion of dandisets currently being published [#1323](https://github.com/dandi/dandi-archive/pull/1323) ([@mvandenburgh](https://github.com/mvandenburgh))
- Render error message in UI when uncaught exception happens [#1320](https://github.com/dandi/dandi-archive/pull/1320) ([@mvandenburgh](https://github.com/mvandenburgh))

#### 🏠 Internal

- Fix mypy errors in `api/admin.py` [#1333](https://github.com/dandi/dandi-archive/pull/1333) ([@mvandenburgh](https://github.com/mvandenburgh))
- [gh-actions](deps): Bump actions/add-to-project from 0.0.3 to 0.3.0 [#1325](https://github.com/dandi/dandi-archive/pull/1325) ([@dependabot[bot]](https://github.com/dependabot[bot]))
- Update GitHub Actions action versions [#1324](https://github.com/dandi/dandi-archive/pull/1324) ([@jwodder](https://github.com/jwodder))

#### 🧪 Tests

- Disable pulling of all Docker images from Docker Hub [#1339](https://github.com/dandi/dandi-archive/pull/1339) ([@jwodder](https://github.com/jwodder))

#### Authors: 6

- [@dependabot[bot]](https://github.com/dependabot[bot])
- Dan LaManna ([@danlamanna](https://github.com/danlamanna))
- Jacob Nesbitt ([@AlmightyYakob](https://github.com/AlmightyYakob))
- John T. Wodder II ([@jwodder](https://github.com/jwodder))
- Mike VanDenburgh ([@mvandenburgh](https://github.com/mvandenburgh))
- Roni Choudhury ([@waxlamp](https://github.com/waxlamp))

---

# v0.2.54 (Tue Oct 11 2022)

#### 🐛 Bug Fix

- Fix 401 errors from `/versions/` endpoint being reported to sentry [#1321](https://github.com/dandi/dandi-archive/pull/1321) ([@mvandenburgh](https://github.com/mvandenburgh))

#### Authors: 1

- Mike VanDenburgh ([@mvandenburgh](https://github.com/mvandenburgh))

---

# v0.2.53 (Thu Oct 06 2022)

#### 🐛 Bug Fix

- Prevent double-publishing [#1006](https://github.com/dandi/dandi-archive/pull/1006) ([@mvandenburgh](https://github.com/mvandenburgh))

#### 🧪 Tests

- Add additional waits to account E2E test [#1310](https://github.com/dandi/dandi-archive/pull/1310) ([@mvandenburgh](https://github.com/mvandenburgh))

#### Authors: 1

- Mike VanDenburgh ([@mvandenburgh](https://github.com/mvandenburgh))

---

# v0.2.52 (Tue Oct 04 2022)

#### 🐛 Bug Fix

- Update frontend to use new query parameter for version listing endpoint [#1309](https://github.com/dandi/dandi-archive/pull/1309) ([@mvandenburgh](https://github.com/mvandenburgh))

#### Authors: 1

- Mike VanDenburgh ([@mvandenburgh](https://github.com/mvandenburgh))

---

# v0.2.51 (Tue Oct 04 2022)

#### 🐛 Bug Fix

- Use `django_filters` instead of DRF for Version viewset filtering [#1308](https://github.com/dandi/dandi-archive/pull/1308) ([@mvandenburgh](https://github.com/mvandenburgh))
- Unpin minio docker image and update env var names [#1307](https://github.com/dandi/dandi-archive/pull/1307) ([@mvandenburgh](https://github.com/mvandenburgh))
- Update e2e test dependencies [#1306](https://github.com/dandi/dandi-archive/pull/1306) ([@mvandenburgh](https://github.com/mvandenburgh))
- Convert dandiset search test to jest/puppeteer, remove pyppeteer config from project [#1300](https://github.com/dandi/dandi-archive/pull/1300) ([@mvandenburgh](https://github.com/mvandenburgh))
- Disable save button in Meditor if no changes have been made [#1302](https://github.com/dandi/dandi-archive/pull/1302) ([@mvandenburgh](https://github.com/mvandenburgh))
- Include rejection reason in rejected user email [#1301](https://github.com/dandi/dandi-archive/pull/1301) ([@mvandenburgh](https://github.com/mvandenburgh))
- Increase time limit for write_manifest_files [#1299](https://github.com/dandi/dandi-archive/pull/1299) ([@danlamanna](https://github.com/danlamanna))
- Fix missing spacing for validation error UI when logged out [#1297](https://github.com/dandi/dandi-archive/pull/1297) ([@mvandenburgh](https://github.com/mvandenburgh))
- Rename file without a trailing space [#1298](https://github.com/dandi/dandi-archive/pull/1298) ([@waxlamp](https://github.com/waxlamp))
- Replace pyppeteer test for cookie behavior with puppeteer test [#1295](https://github.com/dandi/dandi-archive/pull/1295) ([@mvandenburgh](https://github.com/mvandenburgh))
- Turn on mypy for `zarr/admin.py` and `zarr/views/` + fix type errors [#1296](https://github.com/dandi/dandi-archive/pull/1296) ([@mvandenburgh](https://github.com/mvandenburgh))
- Refactor dandiset create/delete methods [#1292](https://github.com/dandi/dandi-archive/pull/1292) ([@danlamanna](https://github.com/danlamanna))
- Revert "Temporarily pin DRF" [#1293](https://github.com/dandi/dandi-archive/pull/1293) ([@danlamanna](https://github.com/danlamanna))
- Convert `DandisetPublish.vue` to `<script setup>` [#1283](https://github.com/dandi/dandi-archive/pull/1283) ([@mvandenburgh](https://github.com/mvandenburgh))
- Make misc fixes to the dandiset ownership email [#1279](https://github.com/dandi/dandi-archive/pull/1279) ([@danlamanna](https://github.com/danlamanna))
- Fix link to download help handbook page [#1289](https://github.com/dandi/dandi-archive/pull/1289) ([@mvandenburgh](https://github.com/mvandenburgh))
- Allow for using django core exceptions with DRF [#1290](https://github.com/dandi/dandi-archive/pull/1290) ([@danlamanna](https://github.com/danlamanna))
- Use `exact` prop consistently [#1285](https://github.com/dandi/dandi-archive/pull/1285) ([@waxlamp](https://github.com/waxlamp))
- Temporarily pin DRF [#1291](https://github.com/dandi/dandi-archive/pull/1291) ([@danlamanna](https://github.com/danlamanna))
- Turn off autoescaping for text/plain emails [#1276](https://github.com/dandi/dandi-archive/pull/1276) ([@danlamanna](https://github.com/danlamanna))

#### Authors: 3

- Dan LaManna ([@danlamanna](https://github.com/danlamanna))
- Mike VanDenburgh ([@mvandenburgh](https://github.com/mvandenburgh))
- Roni Choudhury ([@waxlamp](https://github.com/waxlamp))

---

# v0.2.50 (Thu Sep 22 2022)

#### 🐛 Bug Fix

- Fix asset unembargo method [#1282](https://github.com/dandi/dandi-archive/pull/1282) ([@AlmightyYakob](https://github.com/AlmightyYakob))
- Remove `-s` and `-v` flags from CLI integration test invocation [#1287](https://github.com/dandi/dandi-archive/pull/1287) ([@mvandenburgh](https://github.com/mvandenburgh))
- Don't revalidate version metadata on PUT unless it has changed [#1280](https://github.com/dandi/dandi-archive/pull/1280) ([@mvandenburgh](https://github.com/mvandenburgh))
- Fix `useRouter()` sentry error [#1284](https://github.com/dandi/dandi-archive/pull/1284) ([@mvandenburgh](https://github.com/mvandenburgh))

#### Authors: 2

- Jacob Nesbitt ([@AlmightyYakob](https://github.com/AlmightyYakob))
- Mike VanDenburgh ([@mvandenburgh](https://github.com/mvandenburgh))

---

# v0.2.49 (Mon Sep 19 2022)

#### 🐛 Bug Fix

- Enable sentry performance for frontend [#1270](https://github.com/dandi/dandi-archive/pull/1270) ([@mvandenburgh](https://github.com/mvandenburgh))
- Only suppress 4xx errors in pinia action [#1281](https://github.com/dandi/dandi-archive/pull/1281) ([@mvandenburgh](https://github.com/mvandenburgh))
- Improve edge cases around email greetings [#1275](https://github.com/dandi/dandi-archive/pull/1275) ([@danlamanna](https://github.com/danlamanna))

#### Authors: 2

- Dan LaManna ([@danlamanna](https://github.com/danlamanna))
- Mike VanDenburgh ([@mvandenburgh](https://github.com/mvandenburgh))

---

# v0.2.48 (Tue Sep 13 2022)

#### 🐛 Bug Fix

- Add social accounts to user admin page [#1274](https://github.com/dandi/dandi-archive/pull/1274) ([@danlamanna](https://github.com/danlamanna))
- Use direct foreign keys with django-guardian [#1273](https://github.com/dandi/dandi-archive/pull/1273) ([@danlamanna](https://github.com/danlamanna))
- Make Dandiset sorting account for zarr files [#1271](https://github.com/dandi/dandi-archive/pull/1271) ([@danlamanna](https://github.com/danlamanna))

#### Authors: 1

- Dan LaManna ([@danlamanna](https://github.com/danlamanna))

---

# v0.2.47 (Thu Sep 08 2022)

#### 🐛 Bug Fix

- Fix vuetify console error on DLP [#1269](https://github.com/dandi/dandi-archive/pull/1269) ([@mvandenburgh](https://github.com/mvandenburgh))

#### Authors: 1

- Mike VanDenburgh ([@mvandenburgh](https://github.com/mvandenburgh))

---

# v0.2.46 (Thu Sep 08 2022)

#### 🐛 Bug Fix

- Update Sentry frontend configuration and report error logs [#1268](https://github.com/dandi/dandi-archive/pull/1268) ([@mvandenburgh](https://github.com/mvandenburgh))
- Fix display of validation errors when there's no associated field [#1266](https://github.com/dandi/dandi-archive/pull/1266) ([@danlamanna](https://github.com/danlamanna))
- Migrate Vuex store to Pinia [#1265](https://github.com/dandi/dandi-archive/pull/1265) ([@mvandenburgh](https://github.com/mvandenburgh))
- Fix missing package error when first using docker-compose setup [#1158](https://github.com/dandi/dandi-archive/pull/1158) ([@AlmightyYakob](https://github.com/AlmightyYakob))
- Remove unnecessary conditional check for schemaVersion [#1257](https://github.com/dandi/dandi-archive/pull/1257) ([@danlamanna](https://github.com/danlamanna))
- Convert some vue components to `<script setup>` [#1263](https://github.com/dandi/dandi-archive/pull/1263) ([@mvandenburgh](https://github.com/mvandenburgh))

#### Authors: 3

- Dan LaManna ([@danlamanna](https://github.com/danlamanna))
- Jacob Nesbitt ([@AlmightyYakob](https://github.com/AlmightyYakob))
- Mike VanDenburgh ([@mvandenburgh](https://github.com/mvandenburgh))

---

# v0.2.45 (Thu Sep 01 2022)

#### 🐛 Bug Fix

- Upgrade frontend to Vue 2.7 [#1258](https://github.com/dandi/dandi-archive/pull/1258) ([@mvandenburgh](https://github.com/mvandenburgh))
- Replace `vue-type-check` with `vue-tsc` [#1259](https://github.com/dandi/dandi-archive/pull/1259) ([@mvandenburgh](https://github.com/mvandenburgh))

#### Authors: 1

- Mike VanDenburgh ([@mvandenburgh](https://github.com/mvandenburgh))

---

# v0.2.44 (Wed Aug 31 2022)

#### 🐛 Bug Fix

- Create django app for zarr functionality [#1256](https://github.com/dandi/dandi-archive/pull/1256) ([@danlamanna](https://github.com/danlamanna))
- Rearrange file structure [#1255](https://github.com/dandi/dandi-archive/pull/1255) ([@mvandenburgh](https://github.com/mvandenburgh))
- Remove TODO about Django Sites [#1254](https://github.com/dandi/dandi-archive/pull/1254) ([@mvandenburgh](https://github.com/mvandenburgh))

#### Authors: 2

- Dan LaManna ([@danlamanna](https://github.com/danlamanna))
- Mike VanDenburgh ([@mvandenburgh](https://github.com/mvandenburgh))

---

# v0.2.43 (Thu Aug 25 2022)

#### 🐛 Bug Fix

- Update assets path pagination [#1253](https://github.com/dandi/dandi-archive/pull/1253) ([@AlmightyYakob](https://github.com/AlmightyYakob))
- Fix type errors in `mail.py` [#1250](https://github.com/dandi/dandi-archive/pull/1250) ([@mvandenburgh](https://github.com/mvandenburgh))
- Remove `management/` directory from excluded mypy files [#1252](https://github.com/dandi/dandi-archive/pull/1252) ([@mvandenburgh](https://github.com/mvandenburgh))
- Remove `migrations/` from excluded mypy files [#1251](https://github.com/dandi/dandi-archive/pull/1251) ([@mvandenburgh](https://github.com/mvandenburgh))
- Fix asset list performance issue [#1222](https://github.com/dandi/dandi-archive/pull/1222) ([@danlamanna](https://github.com/danlamanna))
- Fix `target-version` for black [#1249](https://github.com/dandi/dandi-archive/pull/1249) ([@mvandenburgh](https://github.com/mvandenburgh))
- Require Python 3.10 [#1247](https://github.com/dandi/dandi-archive/pull/1247) ([@mvandenburgh](https://github.com/mvandenburgh))
- Fix type errors in `models` [#1246](https://github.com/dandi/dandi-archive/pull/1246) ([@mvandenburgh](https://github.com/mvandenburgh))
- Fix type errors in `tasks` [#1244](https://github.com/dandi/dandi-archive/pull/1244) ([@mvandenburgh](https://github.com/mvandenburgh))
- Update s3-file-field dependency [#1241](https://github.com/dandi/dandi-archive/pull/1241) ([@danlamanna](https://github.com/danlamanna))
- Clean up storage layer [#1238](https://github.com/dandi/dandi-archive/pull/1238) ([@danlamanna](https://github.com/danlamanna))
- Optimize zarr list endpoint [#1220](https://github.com/dandi/dandi-archive/pull/1220) ([@AlmightyYakob](https://github.com/AlmightyYakob) [@danlamanna](https://github.com/danlamanna))
- Remove unused dependency httpx [#1240](https://github.com/dandi/dandi-archive/pull/1240) ([@danlamanna](https://github.com/danlamanna))
- Fix incorrect type hints [#1231](https://github.com/dandi/dandi-archive/pull/1231) ([@mvandenburgh](https://github.com/mvandenburgh))
- Require metadata/asset schemaVersion [#1199](https://github.com/dandi/dandi-archive/pull/1199) ([@danlamanna](https://github.com/danlamanna))
- Fix zarr viewer [#1236](https://github.com/dandi/dandi-archive/pull/1236) ([@mvandenburgh](https://github.com/mvandenburgh))
- Add external viewer for NGFF files [#1067](https://github.com/dandi/dandi-archive/pull/1067) ([@mvandenburgh](https://github.com/mvandenburgh))
- Revert "Pin flake8 version" [#1233](https://github.com/dandi/dandi-archive/pull/1233) ([@mvandenburgh](https://github.com/mvandenburgh))
- changes in ShareDialog: using inline style [#828](https://github.com/dandi/dandi-archive/pull/828) ([@djarecka](https://github.com/djarecka) [@mvandenburgh](https://github.com/mvandenburgh))
- DOC: add DLP abbreviation to initiate Abbreviations in DEVELOPMENT.md [#1224](https://github.com/dandi/dandi-archive/pull/1224) ([@yarikoptic](https://github.com/yarikoptic))
- De-Duplicate API calls in DLP [#1208](https://github.com/dandi/dandi-archive/pull/1208) ([@DeepikaGhodki](https://github.com/DeepikaGhodki))
- Use tuples for Admin model actions and inlines [#1229](https://github.com/dandi/dandi-archive/pull/1229) ([@AlmightyYakob](https://github.com/AlmightyYakob))

#### 🧪 Tests

- Configure mypy [#1243](https://github.com/dandi/dandi-archive/pull/1243) ([@mvandenburgh](https://github.com/mvandenburgh))

#### Authors: 6

- Dan LaManna ([@danlamanna](https://github.com/danlamanna))
- Deepika Ghodki ([@DeepikaGhodki](https://github.com/DeepikaGhodki))
- Dorota Jarecka ([@djarecka](https://github.com/djarecka))
- Jacob Nesbitt ([@AlmightyYakob](https://github.com/AlmightyYakob))
- Mike VanDenburgh ([@mvandenburgh](https://github.com/mvandenburgh))
- Yaroslav Halchenko ([@yarikoptic](https://github.com/yarikoptic))

---

# v0.2.42 (Wed Aug 03 2022)

:tada: This release contains work from a new contributor! :tada:

Thank you, Deepika Ghodki ([@DeepikaGhodki](https://github.com/DeepikaGhodki)), for all your work!

#### 🐛 Bug Fix

- Use an ordered QuerySet in Zarr viewset [#1202](https://github.com/dandi/dandi-archive/pull/1202) ([@waxlamp](https://github.com/waxlamp))
- Navigation buttons on landing page [#1172](https://github.com/dandi/dandi-archive/pull/1172) ([@DeepikaGhodki](https://github.com/DeepikaGhodki))
- Pin flake8 version [#1226](https://github.com/dandi/dandi-archive/pull/1226) ([@AlmightyYakob](https://github.com/AlmightyYakob))
- Remove flake8 linting rule [#1223](https://github.com/dandi/dandi-archive/pull/1223) ([@danlamanna](https://github.com/danlamanna))
- Escape . in regex for EXTERNAL_SERVICES [#1191](https://github.com/dandi/dandi-archive/pull/1191) ([@yarikoptic](https://github.com/yarikoptic))
- Add "/server-info/" frontend endpoint in development builds [#1190](https://github.com/dandi/dandi-archive/pull/1190) ([@waxlamp](https://github.com/waxlamp))

#### Authors: 5

- Dan LaManna ([@danlamanna](https://github.com/danlamanna))
- Deepika Ghodki ([@DeepikaGhodki](https://github.com/DeepikaGhodki))
- Jacob Nesbitt ([@AlmightyYakob](https://github.com/AlmightyYakob))
- Roni Choudhury ([@waxlamp](https://github.com/waxlamp))
- Yaroslav Halchenko ([@yarikoptic](https://github.com/yarikoptic))

---

# v0.2.41 (Wed Jul 27 2022)

:tada: This release contains work from a new contributor! :tada:

Thank you, Deepika Ghodki ([@DeepikaGhodki](https://github.com/DeepikaGhodki)), for all your work!

#### 🐛 Bug Fix

- Add metadata flag for asset listing [#1216](https://github.com/dandi/dandi-archive/pull/1216) ([@AlmightyYakob](https://github.com/AlmightyYakob))
- Handle forbidden characters in asset path [#1201](https://github.com/dandi/dandi-archive/pull/1201) ([@DeepikaGhodki](https://github.com/DeepikaGhodki))
- Add memray dev deps to setup.py [#1143](https://github.com/dandi/dandi-archive/pull/1143) ([@AlmightyYakob](https://github.com/AlmightyYakob))

#### 📝 Documentation

- Update Zarr design doc for changes to checksum format [#1175](https://github.com/dandi/dandi-archive/pull/1175) ([@jwodder](https://github.com/jwodder))

#### Authors: 3

- Deepika Ghodki ([@DeepikaGhodki](https://github.com/DeepikaGhodki))
- Jacob Nesbitt ([@AlmightyYakob](https://github.com/AlmightyYakob))
- John T. Wodder II ([@jwodder](https://github.com/jwodder))

---

# v0.2.40 (Tue Jul 26 2022)

#### 🐛 Bug Fix

- Improve sentry configuration [#1215](https://github.com/dandi/dandi-archive/pull/1215) ([@danlamanna](https://github.com/danlamanna))
- Prefer social account data over direct user data [#1140](https://github.com/dandi/dandi-archive/pull/1140) ([@AlmightyYakob](https://github.com/AlmightyYakob))
- Present dialog if attempting to remove self from dandiset [#1125](https://github.com/dandi/dandi-archive/pull/1125) ([@AlmightyYakob](https://github.com/AlmightyYakob))
- Unpin `numpy` dependency in CLI tests [#1212](https://github.com/dandi/dandi-archive/pull/1212) ([@mvandenburgh](https://github.com/mvandenburgh))
- Fix bug in `import_dandisets` script [#1211](https://github.com/dandi/dandi-archive/pull/1211) ([@mvandenburgh](https://github.com/mvandenburgh))
- Fix partial filename from paths_prefix [#591](https://github.com/dandi/dandi-archive/pull/591) ([@AlmightyYakob](https://github.com/AlmightyYakob))

#### 🏠 Internal

- Properly include "data packages" in project [#1114](https://github.com/dandi/dandi-archive/pull/1114) ([@jwodder](https://github.com/jwodder))

#### Authors: 4

- Dan LaManna ([@danlamanna](https://github.com/danlamanna))
- Jacob Nesbitt ([@AlmightyYakob](https://github.com/AlmightyYakob))
- John T. Wodder II ([@jwodder](https://github.com/jwodder))
- Mike VanDenburgh ([@mvandenburgh](https://github.com/mvandenburgh))

---

# v0.2.39 (Fri Jul 22 2022)

#### 🐛 Bug Fix

- Enable Sentry performance tracking [#1209](https://github.com/dandi/dandi-archive/pull/1209) ([@danlamanna](https://github.com/danlamanna))
- Add ngff rename script as a management command [#1120](https://github.com/dandi/dandi-archive/pull/1120) ([@mvandenburgh](https://github.com/mvandenburgh))
- Add publish "checklist" [#1122](https://github.com/dandi/dandi-archive/pull/1122) ([@mvandenburgh](https://github.com/mvandenburgh))

#### Authors: 2

- Dan LaManna ([@danlamanna](https://github.com/danlamanna))
- Mike VanDenburgh ([@mvandenburgh](https://github.com/mvandenburgh))

---

# v0.2.38 (Tue Jul 19 2022)

#### 🐛 Bug Fix

- Improve manifest file writing performance [#1184](https://github.com/dandi/dandi-archive/pull/1184) ([@danlamanna](https://github.com/danlamanna))
- Add time limits to celery tasks [#1187](https://github.com/dandi/dandi-archive/pull/1187) ([@danlamanna](https://github.com/danlamanna))
- boost copyright to 2022 from 2019 [#893](https://github.com/dandi/dandi-archive/pull/893) ([@yarikoptic](https://github.com/yarikoptic))

#### Authors: 2

- Dan LaManna ([@danlamanna](https://github.com/danlamanna))
- Yaroslav Halchenko ([@yarikoptic](https://github.com/yarikoptic))

---

# v0.2.37 (Tue Jul 12 2022)

#### 🐛 Bug Fix

- Fix admin search fields [#1185](https://github.com/dandi/dandi-archive/pull/1185) ([@danlamanna](https://github.com/danlamanna))
- Fix flaky e2e test [#1178](https://github.com/dandi/dandi-archive/pull/1178) ([@mvandenburgh](https://github.com/mvandenburgh))

#### Authors: 2

- Dan LaManna ([@danlamanna](https://github.com/danlamanna))
- Mike VanDenburgh ([@mvandenburgh](https://github.com/mvandenburgh))

---

# v0.2.36 (Mon Jul 11 2022)

#### 🐛 Bug Fix

- Write manifest files after committing transaction [#1176](https://github.com/dandi/dandi-archive/pull/1176) ([@danlamanna](https://github.com/danlamanna))
- Upgrade django-composed-configuration [#1174](https://github.com/dandi/dandi-archive/pull/1174) ([@danlamanna](https://github.com/danlamanna))
- Allow longer zarr blob names [#1173](https://github.com/dandi/dandi-archive/pull/1173) ([@danlamanna](https://github.com/danlamanna))

#### Authors: 1

- Dan LaManna ([@danlamanna](https://github.com/danlamanna))

---

# v0.2.35 (Mon Jul 11 2022)

:tada: This release contains work from a new contributor! :tada:

Thank you, Dan LaManna ([@danlamanna](https://github.com/danlamanna)), for all your work!

#### 🐛 Bug Fix

- Improve load times of admin pages [#1169](https://github.com/dandi/dandi-archive/pull/1169) ([@danlamanna](https://github.com/danlamanna))

#### Authors: 1

- Dan LaManna ([@danlamanna](https://github.com/danlamanna))

---

# v0.2.34 (Thu Jul 07 2022)

#### 🐛 Bug Fix

- Fix more memory issues in tasks [#1161](https://github.com/dandi/dandi-archive/pull/1161) ([@mvandenburgh](https://github.com/mvandenburgh))
- Use iteration instead of recursion in `import_dandisets` script [#1150](https://github.com/dandi/dandi-archive/pull/1150) ([@mvandenburgh](https://github.com/mvandenburgh))

#### Authors: 1

- Mike VanDenburgh ([@mvandenburgh](https://github.com/mvandenburgh))

---

# v0.2.33 (Thu Jul 07 2022)

#### 🐛 Bug Fix

- Fix race condition in sha256 calculation [#1164](https://github.com/dandi/dandi-archive/pull/1164) ([@mvandenburgh](https://github.com/mvandenburgh) [@AlmightyYakob](https://github.com/AlmightyYakob))

#### Authors: 2

- Jacob Nesbitt ([@AlmightyYakob](https://github.com/AlmightyYakob))
- Mike VanDenburgh ([@mvandenburgh](https://github.com/mvandenburgh))

---

# v0.2.32 (Wed Jul 06 2022)

#### 🐛 Bug Fix

- Optimize dandiset list endpoint [#1134](https://github.com/dandi/dandi-archive/pull/1134) ([@AlmightyYakob](https://github.com/AlmightyYakob))
- adding license field to the create dandiset page [#839](https://github.com/dandi/dandi-archive/pull/839) ([@djarecka](https://github.com/djarecka) [@mvandenburgh](https://github.com/mvandenburgh))

#### Authors: 3

- Dorota Jarecka ([@djarecka](https://github.com/djarecka))
- Jacob Nesbitt ([@AlmightyYakob](https://github.com/AlmightyYakob))
- Mike VanDenburgh ([@mvandenburgh](https://github.com/mvandenburgh))

---

# v0.2.31 (Tue Jul 05 2022)

#### 🐛 Bug Fix

- Fix excessive memory usage in asset summary calculation [#1159](https://github.com/dandi/dandi-archive/pull/1159) ([@mvandenburgh](https://github.com/mvandenburgh))

#### Authors: 1

- Mike VanDenburgh ([@mvandenburgh](https://github.com/mvandenburgh))

---

# v0.2.30 (Fri Jul 01 2022)

#### 🐛 Bug Fix

- Fix missing zarr_id in `cancel_zarr_upload` [#1154](https://github.com/dandi/dandi-archive/pull/1154) ([@AlmightyYakob](https://github.com/AlmightyYakob))

#### Authors: 1

- Jacob Nesbitt ([@AlmightyYakob](https://github.com/AlmightyYakob))

---

# v0.2.29 (Fri Jul 01 2022)

#### 🐛 Bug Fix

- Use `logging.info` for user errors instead of `logging.error` [#1152](https://github.com/dandi/dandi-archive/pull/1152) ([@mvandenburgh](https://github.com/mvandenburgh))
- Add support for cloning assets to `import_dandisets` script [#1131](https://github.com/dandi/dandi-archive/pull/1131) ([@mvandenburgh](https://github.com/mvandenburgh))
- Sort user search results [#1146](https://github.com/dandi/dandi-archive/pull/1146) ([@mvandenburgh](https://github.com/mvandenburgh))

#### Authors: 1

- Mike VanDenburgh ([@mvandenburgh](https://github.com/mvandenburgh))

---

# v0.2.28 (Thu Jun 30 2022)

#### 🐛 Bug Fix

- Revert "Add verbose logging to `ingest_zarr_archive` task" [#1133](https://github.com/dandi/dandi-archive/pull/1133) ([@mvandenburgh](https://github.com/mvandenburgh))

#### Authors: 1

- Mike VanDenburgh ([@mvandenburgh](https://github.com/mvandenburgh))

---

# v0.2.27 (Wed Jun 29 2022)

#### 🐛 Bug Fix

- Optimize loop in checksum task [#1139](https://github.com/dandi/dandi-archive/pull/1139) ([@mvandenburgh](https://github.com/mvandenburgh))

#### Authors: 1

- Mike VanDenburgh ([@mvandenburgh](https://github.com/mvandenburgh))

---

# v0.2.26 (Mon Jun 27 2022)

#### 🐛 Bug Fix

- Fix broken search bar [#1121](https://github.com/dandi/dandi-archive/pull/1121) ([@mvandenburgh](https://github.com/mvandenburgh))
- Restrict user search [#1124](https://github.com/dandi/dandi-archive/pull/1124) ([@AlmightyYakob](https://github.com/AlmightyYakob))
- Add timeout to gunicorn in heroku [#1127](https://github.com/dandi/dandi-archive/pull/1127) ([@mvandenburgh](https://github.com/mvandenburgh))
- Use QuerySet.iterator in asset paths endpoint [#1126](https://github.com/dandi/dandi-archive/pull/1126) ([@mvandenburgh](https://github.com/mvandenburgh))

#### Authors: 2

- Jacob Nesbitt ([@AlmightyYakob](https://github.com/AlmightyYakob))
- Mike VanDenburgh ([@mvandenburgh](https://github.com/mvandenburgh))

---

# v0.2.25 (Wed Jun 22 2022)

#### 🐛 Bug Fix

- Add verbose logging to `ingest_zarr_archive` task [#1128](https://github.com/dandi/dandi-archive/pull/1128) ([@mvandenburgh](https://github.com/mvandenburgh))

#### Authors: 1

- Mike VanDenburgh ([@mvandenburgh](https://github.com/mvandenburgh))

---

# v0.2.24 (Tue Jun 21 2022)

#### 🐛 Bug Fix

- Fix improper escaping of glob parameter, remove regex search [#1062](https://github.com/dandi/dandi-archive/pull/1062) ([@mvandenburgh](https://github.com/mvandenburgh))
- ENH: increase page size from 25 to 100 [#1107](https://github.com/dandi/dandi-archive/pull/1107) ([@yarikoptic](https://github.com/yarikoptic))

#### Authors: 2

- Mike VanDenburgh ([@mvandenburgh](https://github.com/mvandenburgh))
- Yaroslav Halchenko ([@yarikoptic](https://github.com/yarikoptic))

---

# v0.2.23 (Thu May 12 2022)

#### ⚠️ Pushed to `master`

- Empty commit without markers to skip ci to see if release would be released on netlify ([@yarikoptic](https://github.com/yarikoptic))

#### 🏠 Internal

- BF: provide custom commit message without token to skip the beat [#1101](https://github.com/dandi/dandi-archive/pull/1101) ([@yarikoptic](https://github.com/yarikoptic))

#### Authors: 1

- Yaroslav Halchenko ([@yarikoptic](https://github.com/yarikoptic))

---

# v0.2.22 (Thu May 12 2022)

#### 🏠 Internal

- BF: production-deploy - add "needs" dependency within update-release-branch [#1099](https://github.com/dandi/dandi-archive/pull/1099) ([@yarikoptic](https://github.com/yarikoptic))

#### Authors: 1

- Yaroslav Halchenko ([@yarikoptic](https://github.com/yarikoptic))

---

# v0.2.21 (Wed May 11 2022)

#### 🐛 Bug Fix

- checking the validation status, new attempt [#1097](https://github.com/dandi/dandi-archive/pull/1097) ([@djarecka](https://github.com/djarecka))
- Fix opening Meditor when clicking on "Fix Issues" in the list of dandiset metadata issues [#1088](https://github.com/dandi/dandi-archive/pull/1088) ([@djarecka](https://github.com/djarecka))
- BF(workaround): to avoid crash for user lacking metadata - return INCOMPLETE [#1086](https://github.com/dandi/dandi-archive/pull/1086) ([@yarikoptic](https://github.com/yarikoptic))
- Remove EmbargoedZarrArchive since not supported [#1077](https://github.com/dandi/dandi-archive/pull/1077) ([@yarikoptic](https://github.com/yarikoptic))
- TST: added a test and tune up to factories to ensure that zarr size is computed [#1077](https://github.com/dandi/dandi-archive/pull/1077) ([@yarikoptic](https://github.com/yarikoptic))
- BF: add {Embragoed,}ZarrArchive sizes into total_size compute [#1077](https://github.com/dandi/dandi-archive/pull/1077) ([@yarikoptic](https://github.com/yarikoptic))
- RF: avoid code duplication while considering two types of *AssetBlobs [#1077](https://github.com/dandi/dandi-archive/pull/1077) ([@yarikoptic](https://github.com/yarikoptic))

#### 📝 Documentation

- BF DOC(incomplete): /zarr/.../ingest has 204 not 200 response [#1087](https://github.com/dandi/dandi-archive/pull/1087) ([@yarikoptic](https://github.com/yarikoptic))
- Extend docs with information about devel env [#1084](https://github.com/dandi/dandi-archive/pull/1084) ([@yarikoptic](https://github.com/yarikoptic))

#### Authors: 2

- Dorota Jarecka ([@djarecka](https://github.com/djarecka))
- Yaroslav Halchenko ([@yarikoptic](https://github.com/yarikoptic))

---

# v0.2.20 (Thu May 05 2022)

#### 🐛 Bug Fix

- Empty commit to cut a release [#1082](https://github.com/dandi/dandi-archive/pull/1082) ([@yarikoptic](https://github.com/yarikoptic))
- Boost dandischema and DANDI_SCHEMA_VERSION [#1074](https://github.com/dandi/dandi-archive/pull/1074) ([@yarikoptic](https://github.com/yarikoptic) [@AlmightyYakob](https://github.com/AlmightyYakob))
- Remove erroneous select_for_update and update tests to use transactions [#1066](https://github.com/dandi/dandi-archive/pull/1066) ([@AlmightyYakob](https://github.com/AlmightyYakob))

#### Authors: 2

- Jacob Nesbitt ([@AlmightyYakob](https://github.com/AlmightyYakob))
- Yaroslav Halchenko ([@yarikoptic](https://github.com/yarikoptic))

---

# v0.2.19 (Fri Apr 29 2022)

#### 🐛 Bug Fix

- Deploy to heroku with Heroku CLI directly [#1075](https://github.com/dandi/dandi-archive/pull/1075) ([@AlmightyYakob](https://github.com/AlmightyYakob))

#### Authors: 1

- Jacob Nesbitt ([@AlmightyYakob](https://github.com/AlmightyYakob))

---

# v0.2.18 (Fri Apr 29 2022)

#### 🐛 Bug Fix

- Fix version in `/api/info/` [#1054](https://github.com/dandi/dandi-archive/pull/1054) ([@AlmightyYakob](https://github.com/AlmightyYakob))
- Fix failing `test_create_dev_dandiset` [#1070](https://github.com/dandi/dandi-archive/pull/1070) ([@AlmightyYakob](https://github.com/AlmightyYakob))
- Pin django-oauth-toolkit to 1.x [#1072](https://github.com/dandi/dandi-archive/pull/1072) ([@waxlamp](https://github.com/waxlamp))
- Add garbage collection design doc [#560](https://github.com/dandi/dandi-archive/pull/560) ([@dchiquito](https://github.com/dchiquito))
- Handle missing location query param [#1069](https://github.com/dandi/dandi-archive/pull/1069) ([@AlmightyYakob](https://github.com/AlmightyYakob))
- Add actions workflow to auto-add issues to beta project board [#1043](https://github.com/dandi/dandi-archive/pull/1043) ([@waxlamp](https://github.com/waxlamp))
- Misc. Django/Python improvements [#1050](https://github.com/dandi/dandi-archive/pull/1050) ([@mvandenburgh](https://github.com/mvandenburgh))

#### Authors: 4

- Daniel Chiquito ([@dchiquito](https://github.com/dchiquito))
- Jacob Nesbitt ([@AlmightyYakob](https://github.com/AlmightyYakob))
- Mike VanDenburgh ([@mvandenburgh](https://github.com/mvandenburgh))
- Roni Choudhury ([@waxlamp](https://github.com/waxlamp))

---

# v0.2.17 (Thu Apr 21 2022)

#### 🐛 Bug Fix

- Remove trailing slash in info api url [#1056](https://github.com/dandi/dandi-archive/pull/1056) ([@AlmightyYakob](https://github.com/AlmightyYakob))

#### Authors: 1

- Jacob Nesbitt ([@AlmightyYakob](https://github.com/AlmightyYakob))

---

# v0.2.16 (Wed Apr 20 2022)

#### 🐛 Bug Fix

- Change `UserMetadata.user` on_delete to `CASCADE` [#1053](https://github.com/dandi/dandi-archive/pull/1053) ([@mvandenburgh](https://github.com/mvandenburgh))
- Add configuration for deploy previews to `netlify.toml` [#1051](https://github.com/dandi/dandi-archive/pull/1051) ([@mvandenburgh](https://github.com/mvandenburgh))

#### Authors: 1

- Mike VanDenburgh ([@mvandenburgh](https://github.com/mvandenburgh))

---

# v0.2.15 (Wed Apr 20 2022)

#### 🐛 Bug Fix

- Include `api/` suffix in info endpoint api url [#1049](https://github.com/dandi/dandi-archive/pull/1049) ([@AlmightyYakob](https://github.com/AlmightyYakob))

#### Authors: 1

- Jacob Nesbitt ([@AlmightyYakob](https://github.com/AlmightyYakob))

---

# v0.2.14 (Wed Apr 20 2022)

#### 🐛 Bug Fix

- Fix incorrect fields in info endpoint [#1046](https://github.com/dandi/dandi-archive/pull/1046) ([@AlmightyYakob](https://github.com/AlmightyYakob))
- Select all underlying asset storage fields in asset paths endpoint [#1034](https://github.com/dandi/dandi-archive/pull/1034) ([@AlmightyYakob](https://github.com/AlmightyYakob))

#### Authors: 1

- Jacob Nesbitt ([@AlmightyYakob](https://github.com/AlmightyYakob))

---

# v0.2.13 (Tue Apr 19 2022)

#### 🐛 Bug Fix

- Empty commit to trigger release [#1042](https://github.com/dandi/dandi-archive/pull/1042) ([@AlmightyYakob](https://github.com/AlmightyYakob))
- Add new netlify redirector [#1028](https://github.com/dandi/dandi-archive/pull/1028) ([@AlmightyYakob](https://github.com/AlmightyYakob))
- Add netlify plugin and redirection [#1018](https://github.com/dandi/dandi-archive/pull/1018) ([@AlmightyYakob](https://github.com/AlmightyYakob))
- Replace use of strip with lstrip [#1041](https://github.com/dandi/dandi-archive/pull/1041) ([@AlmightyYakob](https://github.com/AlmightyYakob))
- Add support for glob/regex filtering on `NestedAsset` list endpoint [#1022](https://github.com/dandi/dandi-archive/pull/1022) ([@mvandenburgh](https://github.com/mvandenburgh))

#### Authors: 2

- Jacob Nesbitt ([@AlmightyYakob](https://github.com/AlmightyYakob))
- Mike VanDenburgh ([@mvandenburgh](https://github.com/mvandenburgh))

---

# v0.2.11 (Mon Apr 18 2022)

#### 🐛 Bug Fix

- Push to heroku directly in update-release-branch.yml [#1038](https://github.com/dandi/dandi-archive/pull/1038) ([@AlmightyYakob](https://github.com/AlmightyYakob))

#### Authors: 1

- Jacob Nesbitt ([@AlmightyYakob](https://github.com/AlmightyYakob))

---

# v0.2.10 (Mon Apr 18 2022)

#### 🐛 Bug Fix

- Fix disabled Heroku Github integration for staging and production deployment [#1036](https://github.com/dandi/dandi-archive/pull/1036) ([@AlmightyYakob](https://github.com/AlmightyYakob))

#### Authors: 1

- Jacob Nesbitt ([@AlmightyYakob](https://github.com/AlmightyYakob))

---

# v0.2.8 (Fri Apr 15 2022)

#### 🐛 Bug Fix

- Release branch CI [#1033](https://github.com/dandi/dandi-archive/pull/1033) ([@dchiquito](https://github.com/dchiquito) [@AlmightyYakob](https://github.com/AlmightyYakob))
- Deployment design doc [#1024](https://github.com/dandi/dandi-archive/pull/1024) ([@dchiquito](https://github.com/dchiquito) [@dandibot](https://github.com/dandibot))

#### Authors: 3

- Dandi Bot ([@dandibot](https://github.com/dandibot))
- Daniel Chiquito ([@dchiquito](https://github.com/dchiquito))
- Jacob Nesbitt ([@AlmightyYakob](https://github.com/AlmightyYakob))

---

# v0.2.8 (Thu Apr 14 2022)

#### 🐛 Bug Fix

- Fix responsiveness of v-app-bar [#1014](https://github.com/dandi/dandi-archive/pull/1014) ([@jtomeck](https://github.com/jtomeck) [@mvandenburgh](https://github.com/mvandenburgh))
- Create design doc for replacing Redirector with Netlify [#1017](https://github.com/dandi/dandi-archive/pull/1017) ([@AlmightyYakob](https://github.com/AlmightyYakob))
- Add name and dandiset filtering to zarr list endpoint [#1000](https://github.com/dandi/dandi-archive/pull/1000) ([@AlmightyYakob](https://github.com/AlmightyYakob))
- Add force argument in `ingest_zarr_archive` [#1010](https://github.com/dandi/dandi-archive/pull/1010) ([@AlmightyYakob](https://github.com/AlmightyYakob))
- Use history mode instead of hash mode (remove hash from GUI URL) [#997](https://github.com/dandi/dandi-archive/pull/997) ([@AlmightyYakob](https://github.com/AlmightyYakob))
- Fix Vue lint step in CI [#1015](https://github.com/dandi/dandi-archive/pull/1015) ([@mvandenburgh](https://github.com/mvandenburgh))
- Set up pyppeteer e2e tests [#990](https://github.com/dandi/dandi-archive/pull/990) ([@mvandenburgh](https://github.com/mvandenburgh))

#### Authors: 3

- Jacob Nesbitt ([@AlmightyYakob](https://github.com/AlmightyYakob))
- Jared Tomeck ([@jtomeck](https://github.com/jtomeck))
- Mike VanDenburgh ([@mvandenburgh](https://github.com/mvandenburgh))

---

# v0.2.7 (Wed Apr 06 2022)

#### 🐛 Bug Fix

- Remove `models.PROTECT` from `Asset.previous` [#1009](https://github.com/dandi/dandi-archive/pull/1009) ([@mvandenburgh](https://github.com/mvandenburgh))

#### Authors: 1

- Mike VanDenburgh ([@mvandenburgh](https://github.com/mvandenburgh))

---

# v0.2.6 (Wed Apr 06 2022)

#### 🐛 Bug Fix

- Fix search bar overflowing offscreen [#1008](https://github.com/dandi/dandi-archive/pull/1008) ([@mvandenburgh](https://github.com/mvandenburgh))

#### Authors: 1

- Mike VanDenburgh ([@mvandenburgh](https://github.com/mvandenburgh))

---

# v0.2.5 (Wed Apr 06 2022)

#### 🐛 Bug Fix

- Make checksum_worker responsible for zarr ingest [#1005](https://github.com/dandi/dandi-archive/pull/1005) ([@dchiquito](https://github.com/dchiquito))

#### Authors: 1

- Daniel Chiquito ([@dchiquito](https://github.com/dchiquito))

---

# v0.2.4 (Wed Apr 06 2022)

#### 🐛 Bug Fix

- Handle validation errors when fetching zarr checksums [#1007](https://github.com/dandi/dandi-archive/pull/1007) ([@dchiquito](https://github.com/dchiquito))

#### Authors: 1

- Daniel Chiquito ([@dchiquito](https://github.com/dchiquito))

---

# v0.2.3 (Wed Apr 06 2022)

#### 🐛 Bug Fix

- Bump dandischema to 0.6.0 [#991](https://github.com/dandi/dandi-archive/pull/991) ([@dchiquito](https://github.com/dchiquito))

#### Authors: 1

- Daniel Chiquito ([@dchiquito](https://github.com/dchiquito))

---

# v0.2.2 (Tue Apr 05 2022)

#### 🐛 Bug Fix

- Allow github login with GET request [#999](https://github.com/dandi/dandi-archive/pull/999) ([@mvandenburgh](https://github.com/mvandenburgh))
- Add manifest-worker to Celery in dev environment [#994](https://github.com/dandi/dandi-archive/pull/994) ([@dchiquito](https://github.com/dchiquito))
- Make publishing an atomic operation [#978](https://github.com/dandi/dandi-archive/pull/978) ([@mvandenburgh](https://github.com/mvandenburgh))

#### Authors: 2

- Daniel Chiquito ([@dchiquito](https://github.com/dchiquito))
- Mike VanDenburgh ([@mvandenburgh](https://github.com/mvandenburgh))

---

# v0.2.1 (Tue Mar 29 2022)

#### 🐛 Bug Fix

- Empty commit to cut a release [#989](https://github.com/dandi/dandi-archive/pull/989) ([@mvandenburgh](https://github.com/mvandenburgh))

#### Authors: 1

- Mike VanDenburgh ([@mvandenburgh](https://github.com/mvandenburgh))

---

# v0.2.0 (Tue Mar 29 2022)

#### 🚀 Enhancement

- Cut a release [#988](https://github.com/dandi/dandi-archive/pull/988) ([@mvandenburgh](https://github.com/mvandenburgh))
- Empty commit to cut a release [#986](https://github.com/dandi/dandi-archive/pull/986) ([@mvandenburgh](https://github.com/mvandenburgh))
- Empty commit to cut release (again) [#984](https://github.com/dandi/dandi-archive/pull/984) ([@mvandenburgh](https://github.com/mvandenburgh))
- Empty commit to cut a release [#982](https://github.com/dandi/dandi-archive/pull/982) ([@mvandenburgh](https://github.com/mvandenburgh))
- Use custom github token for auto release workflow [#979](https://github.com/dandi/dandi-archive/pull/979) ([@mvandenburgh](https://github.com/mvandenburgh))
- Use `intuit/auto` to manage releases [#973](https://github.com/dandi/dandi-archive/pull/973) ([@mvandenburgh](https://github.com/mvandenburgh))

#### 🐛 Bug Fix

- Use PAT when checking out repo in release workflow [#987](https://github.com/dandi/dandi-archive/pull/987) ([@mvandenburgh](https://github.com/mvandenburgh))
- Use dandibot auto token [#981](https://github.com/dandi/dandi-archive/pull/981) ([@mvandenburgh](https://github.com/mvandenburgh))

#### Authors: 1

- Mike VanDenburgh ([@mvandenburgh](https://github.com/mvandenburgh))
