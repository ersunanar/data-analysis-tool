<template>
  <div>
    <vue-pivottable
      :data="items"
      aggregatorName="Count"
      rendererName="Table"
      :rows="[]"
      :cols="[]"
      :vals="[]"
    >
    </vue-pivottable>

    <vue-pivottable-ui
      :data="items"
      aggregatorName="Count"
      rendererName="Table"
      :rows="[]"
      :cols="[]"
      :vals="[]"
    >
    </vue-pivottable-ui>
  </div>
</template>

<script>
import { VuePivottableUi, VuePivottable } from "vue-pivottable";
import "vue-pivottable/dist/vue-pivottable.css";
export default {
  components: {
    VuePivottableUi,
    VuePivottable,
  },

  props: ["items"],
};
</script>
