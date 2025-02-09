import Vue, { computed, ref } from 'vue';
import { EditorInterface } from './editor';

// NOTE: it would be better to use a single ref here instead of seperate state/computed
// variables, but doing so introduces a strange bug where editorInterface.basicModel is
// un-reffed immediately after instantiation. This does not occur when using a computed
// variable with a seperate state object, so we do that here as a workaround.
const state = {
  editorInterface: null as EditorInterface | null,
};

const editorInterface = computed({
  get: () => state.editorInterface,
  set: (newVal) => {
    if (!state.editorInterface) {
      // If editorInterface hasn't been instantiated yet, just assign the new instance to it
      state.editorInterface = newVal;
    } else {
      if (!newVal) {
        return;
      }
      // Otherwise, mutate the existing instance's properties using Vue.set
      Object.entries(newVal).forEach(([key, value]) => {
        Vue.set(state.editorInterface as EditorInterface, key, value);
      });
    }
  },
});

const open = ref(false); // whether or not the Meditor is open

export {
  editorInterface,
  open,
};
