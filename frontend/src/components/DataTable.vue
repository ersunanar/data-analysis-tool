<template>
  <div>
    <div v-if="items.length">
      <b-row>
        <b-col lg="12" class="my-1">
          <b-input-group size="sm">
            <b-form-input
              id="filter-input"
              v-model="filter"
              type="search"
              placeholder="Type to Search"
              debounce="500" 
            ></b-form-input>

            <b-input-group-append>
              <b-button :disabled="!filter" @click="filter = ''">Clear</b-button>
            </b-input-group-append>
          </b-input-group>
        </b-col>

        <br />
        <br />
        <br />

        <p style="font-size : 14px" align="justify">
          <strong> Filter On: </strong>
          <span style="color:grey">
            <i>(leave all unchecked to filter on all data)</i>
          </span>
        </p>
        <div align="justify" inline>
          <div
            class="form-check form-check-inline"
            v-for="i in column_values"
            :key="i"
            :value="i"
            inline
          >
            <input
              v-model="filterOn"
              class="form-check-input"
              type="checkbox"
              :id="i"
              :value="i"
            />
            <label style="font-size : 12px" class="form-check-label" :for="i">{{i.toLowerCase()}}</label>
          </div>
        </div>
      </b-row>

      <br />
      <br />

      <b-table
        
        sticky-header
        style="font-size : 12px"
        max-height="1000px"
        :items="items"
        :fields="fields"
        :current-page="currentPage"
        :per-page="perPage"
        :filter="filter"
        :filter-included-fields="filterOn"
        :sort-by.sync="sortBy"
        :sort-desc.sync="sortDesc"
        :sort-direction="sortDirection"
        show-empty
        @filtered="onFiltered"
        font-size="sm"
        small
      >
      
      <!--  -->
        <template #table-busy>
          <div class="text-center text-danger my-2">
            <b-spinner class="align-middle"></b-spinner>
            <strong>Loading...</strong>
          </div>
        </template>
        
      </b-table>

      <b-pagination
        v-model="currentPage"
        :total-rows="totalRows"
        :per-page="perPage"
        first-text="First"
        prev-text="Prev"
        next-text="Next"
        last-text="Last"
        
      ></b-pagination>

      <div align="left">
        <b-form-select
          style="height:30px;width:100px;color:blue;"
          id="per-page-select"
          v-model="perPage"
          :options="pageOptions"
          size="sm"
        ></b-form-select>
      </div>

    </div>
  </div>
</template>

<script>
export default {
  name: "DataTable",
  props: ["items", "fields", "column_values"],
  data() {
    return {
      totalRows: 1,
      currentPage: 1,
      perPage: 25,
      pageOptions: [10, 25, 50, 100],
      sortBy: "",
      sortDesc: false,
      sortDirection: "asc",
      filter: null,
      filterOn: [],
      infoModal: {
        id: "info-modal",
        title: "",
        content: "",
      },
      options: [
        { text: "Orange", value: "orange" },
        { text: "Apple", value: "apple" },
        { text: "Pineapple", value: "pineapple" },
        { text: "Grape", value: "grape" },
      ],
      timer: 1000
    };
  },

  methods: {
    info(item, index, button) {
      this.infoModal.title = `Row index: ${index}`;
      this.infoModal.content = JSON.stringify(item, null, 2);
      this.$root.$emit("bv::show::modal", this.infoModal.id, button);
    },
    resetInfoModal() {
      this.infoModal.title = "";
      this.infoModal.content = "";
    },
    onFiltered(filteredItems) {
      // Trigger pagination to update the number of buttons/pages due to filtering
      this.totalRows = filteredItems.length;
      this.currentPage = 1;
    },
  },

  computed: {
    sortOptions() {
      // Create an options list from our fields
      return this.fields
        .filter((f) => f.sortable)
        .map((f) => {
          return { text: f.key, value: f.key };
        });
    },

  },

mounted() {

  console.log(this.totalRows)

}



};
</script>

<style>
.sr-only {
  display: none;
}
</style>
