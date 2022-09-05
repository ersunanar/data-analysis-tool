<template>
  <div>
    <div>
      <div align="left">
        <button @click="addDataset()">Add Dataset</button>
        &nbsp;&nbsp;
        <button @click="removeDataset()">Remove Dataset</button>
        &nbsp;&nbsp;
        <button @click="fillData()">Show Datas</button>
      </div>
      <br />

      <!---------------------------------------------------------- ROW-1  --------------------------------------->

      <tr class="criteria">
        <td>
          <strong>DataSet-1 =></strong>
        </td>
        <td>
          <label for="value_for_x"> <strong>X-axis:</strong></label>
        </td>

        <td>
          <select id="value_for_x" @change="getXAxisValue($event)">
            <option value="">Choose for X-axis</option>
            <option v-for="col in column_values" :value="col" :key="col">{{
              col
            }}</option>
          </select>
        </td>

        <td>
          <label for="value_for_y"> <strong> Y-axis:</strong></label>
        </td>

        <td>
          <select id="value_for_y" @change="getYAxisValue($event)">
            <option value="">Choose for Y-axis</option>
            <option v-for="col in column_values" :value="col" :key="col">{{
              col
            }}</option>
          </select>
        </td>

        <td>
          <label for="chart-type"> <strong>Chart Type:</strong> </label>
        </td>

        <td>
          <div align="left">
            <label
              ><input
                type="radio"
                name="chart-type"
                value="bar"
                @change="getChartType($event)"
                checked
              />
              &nbsp;Bar</label
            >
            &nbsp;
            <label
              ><input
                type="radio"
                name="chart-type"
                value="line"
                @change="getChartType($event)"
              />
              &nbsp;Line</label
            >
            &nbsp;
            <label
              ><input
                type="radio"
                name="chart-type"
                value="pie"
                @change="getChartType($event)"
              />
              &nbsp;Pie</label
            >
          </div>
        </td>

        <td>
          <label for="math-method"> <strong>Method:</strong> </label>
        </td>

        <td>
          <div align="left">
            <label
              ><input
                type="radio"
                name="math-method"
                value="sum"
                @change="getMathMethod($event)"
              />
              &nbsp;Sum</label
            >
            &nbsp;
            <label
              ><input
                type="radio"
                name="math-method"
                value="count"
                @change="getMathMethod($event)"
                checked
              />
              &nbsp;Count</label
            >
            &nbsp;
            <label
              ><input
                type="radio"
                name="math-method"
                value="average"
                @change="getMathMethod($event)"
              />
              &nbsp;Average</label
            >
          </div>
        </td>

        <td>
          <label for="filter_by1"><strong>Filter By</strong> </label>
        </td>

        <td>
          <select id="filter_by1" @change="getColumnForFilter1($event)">
            <option value="">choose column</option>
            <option v-for="col in column_values" :value="col" :key="col">{{
              col
            }}</option>
          </select>
        </td>

        <td>
          <select id="filter_by1" @change="getValueForFilter1($event)">
            <option value="">choose value</option>
            <option v-for="val1 in filter_values1" :value="val1" :key="val1">{{
              val1
            }}</option>
          </select>
        </td>

        <td>
          <label v-if="math_method !== 'average'" for="percentage1"
            ><input
              type="checkbox"
              id="percentage1"
              name="percentage1"
              value="percentage"
              @change="getPercentage1()"
            /><strong>&nbsp;show as percentage</strong></label
          >
        </td>

        <td>
          <label v-if="chart_type === 'line'" for="filled1"
            ><input
              type="checkbox"
              id="filled1"
              name="filled1"
              value="filled1"
              @change="getFilledLineChart1()"
            /><strong>&nbsp;filled-line</strong></label
          >
        </td>
      </tr>

      <!---------------------------------------------------------- ROW-2  --------------------------------------->

      <tr class="criteria" v-if="dataset2_added">
        <td>
          <strong>DataSet-2 =></strong>
        </td>
        <td></td>

        <td></td>

        <td>
          <label for="value_for_y2"> <strong>Y-axis:</strong></label>
        </td>

        <td>
          <select id="value_for_y2" @change="getYAxisValue2($event)">
            <option value="">Choose for Y-axis</option>
            <option v-for="col in column_values" :value="col" :key="col">{{
              col
            }}</option>
          </select>
        </td>

        <td>
          <label for="chart-type2"> <strong>Chart Type:</strong> </label>
        </td>

        <td>
          <div align="left">
            <label
              ><input
                type="radio"
                name="chart-type2"
                value="bar"
                @change="getChartType2($event)"
                checked
              />
              &nbsp;Bar</label
            >
            &nbsp;
            <label
              ><input
                type="radio"
                name="chart-type2"
                value="line"
                @change="getChartType2($event)"
              />
              &nbsp;Line</label
            >
          </div>
        </td>

        <td>
          <label for="math-method2"> <strong>Method:</strong> </label>
        </td>

        <td>
          <div align="left">
            <label
              ><input
                type="radio"
                name="math-method2"
                value="sum"
                @change="getMathMethod2($event)"
              />
              Sum</label
            >
            &nbsp;
            <label
              ><input
                type="radio"
                name="math-method2"
                value="count"
                @change="getMathMethod2($event)"
                checked
              />
              &nbsp;Count</label
            >
            &nbsp;
            <label
              ><input
                type="radio"
                name="math-method2"
                value="average"
                @change="getMathMethod2($event)"
              />
              &nbsp;Average</label
            >
          </div>
        </td>

        <td>
          <label for="filter_by2"><strong>Filter By</strong> </label>
        </td>

        <td>
          <select id="filter_by2" @change="getColumnForFilter2($event)">
            <option value="">choose column</option>
            <option v-for="col in column_values" :value="col" :key="col">{{
              col
            }}</option>
          </select>
        </td>

        <td>
          <select id="filter_by2" @change="getValueForFilter2($event)">
            <option value="">choose value</option>
            <option v-for="val2 in filter_values2" :value="val2" :key="val2">{{
              val2
            }}</option>
          </select>
        </td>

        <td>
          <label v-if="math_method2 !== 'average'" for="percentage2"
            ><input
              type="checkbox"
              id="percentage2"
              name="percentage2"
              value="percentage"
              @change="getPercentage2()"
            /><strong>&nbsp;show as percentage</strong></label
          >
        </td>

        <td>
          <label v-if="chart_type2 === 'line'" for="filled2"
            ><input
              type="checkbox"
              id="filled2"
              name="filled2"
              value="filled2"
              @change="getFilledLineChart2()"
            /><strong>&nbsp;filled-line</strong></label
          >
        </td>

        <!---------------------------------------------------------- ROW-3  --------------------------------------->
      </tr>

      <tr class="criteria" v-if="dataset3_added">
        <td>
          <strong>DataSet-3 =></strong>
        </td>

        <td></td>

        <td></td>

        <td>
          <label for="value_for_y3"><strong>Y-axis:</strong></label>
        </td>

        <td>
          <select id="value_for_y3" @change="getYAxisValue3($event)">
            <option value="">Choose for Y-axis</option>
            <option v-for="col in column_values" :value="col" :key="col">{{
              col
            }}</option>
          </select>
        </td>

        <td>
          <label for="chart-type3"> <strong>Chart Type:</strong> </label>
        </td>

        <td>
          <div align="left">
            <label
              ><input
                type="radio"
                name="chart-type3"
                value="bar"
                @change="getChartType3($event)"
                checked
              />
              &nbsp;Bar</label
            >
            &nbsp;
            <label
              ><input
                type="radio"
                name="chart-type3"
                value="line"
                @change="getChartType3($event)"
              />
              &nbsp;Line</label
            >
          </div>
        </td>

        <td>
          <label for="math-method3"> <strong>Method:</strong> </label>
        </td>

        <td>
          <div align="left">
            <label
              ><input
                type="radio"
                name="math-method3"
                value="sum"
                @change="getMathMethod3($event)"
              />&nbsp;Sum</label
            >
            &nbsp;
            <label
              ><input
                type="radio"
                name="math-method3"
                value="count"
                @change="getMathMethod3($event)"
                checked
              />&nbsp;Count</label
            >
            &nbsp;
            <label
              ><input
                type="radio"
                name="math-method3"
                value="average"
                @change="getMathMethod3($event)"
              />&nbsp;Average</label
            >
          </div>
        </td>

        <td>
          <label for="filter_by3"><strong>Filter By</strong> </label>
        </td>

        <td>
          <select id="filter_by3" @change="getColumnForFilter3($event)">
            <option value="">choose column</option>
            <option v-for="col in column_values" :value="col" :key="col">{{
              col
            }}</option>
          </select>
        </td>

        <td>
          <select id="filter_by3" @change="getValueForFilter3($event)">
            <option value="">choose value</option>
            <option v-for="val3 in filter_values3" :value="val3" :key="val3">{{
              val3
            }}</option>
          </select>
        </td>

        <td>
          <label v-if="math_method3 !== 'average'" for="percentage3"
            ><input
              type="checkbox"
              id="percentage3"
              name="percentage3"
              value="percentage"
              @change="getPercentage3()"
            /><strong>&nbsp;show as percentage</strong></label
          >
        </td>

        <td>
          <label v-if="chart_type3 === 'line'" for="filled3"
            ><input
              type="checkbox"
              id="filled3"
              name="filled3"
              value="filled3"
              @change="getFilledLineChart3()"
            /><strong>&nbsp;filled-line</strong></label
          >
        </td>
      </tr>
    </div>

    <br />

    <div v-if="x_axis_value !== '' && y_axis_value !== ''">
      <chart-bar
        ref="chartRef"
        v-if="chart_type == 'bar'"
        :chart-data="datacollection"
        :options="options"
      ></chart-bar>

      <chart-pie
        ref="chartRef"
        v-if="chart_type == 'pie'"
        :chart-data="datacollection"
        :options="options"
      ></chart-pie>

      <chart-line
        ref="chartRef"
        v-if="chart_type == 'line'"
        :chart-data="datacollection"
        :options="options"
      ></chart-line>
    </div>
  </div>
</template>

<!-- ********************************** SCRIPT ************************************ -->

<script>
import ChartBar from "@/components/ChartBar.vue";
import ChartPie from "@/components/ChartPie.vue";
import ChartLine from "@/components/ChartLine.vue";

export default {
  name: "ChartView",
  props: ["items", "column_values"],
  components: { ChartBar, ChartPie, ChartLine },
  data() {
    return {
      datacollection: {},

      x_axis_value: "",
      y_axis_value: "",
      math_method: "count",
      chart_type: "bar",
      data_for_chart: {},
      data_for_labels: [],
      data_label: "",
      data_for_datas: ["x"],
      backgroundColor1: [],
      borderColor1: [],
      filter_values1: [],
      selected_filter_column1: "",
      selected_filter_value1: "",
      percentage1: "",

      dataset1: {
        label: this.math_method + " of " + this.y_axis_value,
        type: "bar",
        fill: false,
        backgroundColor: ["rgba(255, 99, 132, 0.2)"],
        borderColor: ["rgba(255, 99, 132, 1)"],
        data: ["x"],
      },

      dataset2_added: false,
      x_axis_value2: "",
      y_axis_value2: "",
      math_method2: "count",
      chart_type2: "bar",
      data_for_chart2: {},
      data_for_datas2: ["x"],
      backgroundColor2: [],
      borderColor2: [],
      filter_values2: [],
      selected_filter_column2: "",
      selected_filter_value2: "",
      percentage2: "",

      dataset2: {
        label: this.math_method2 + " of " + this.y_axis_value2,
        type: "bar",
        fill: false,
        backgroundColor: ["rgba(75, 192, 192, 0.2)"],
        borderColor: ["rgba(75, 192, 192, 1)"],
        data: ["x"],
      },

      dataset3_added: false,
      x_axis_value3: "",
      y_axis_value3: "",
      math_method3: "count",
      chart_type3: "bar",
      data_for_chart3: {},
      data_for_datas3: ["x"],
      backgroundColor3: [],
      borderColor3: [],
      filter_values3: [],
      selected_filter_column3: "",
      selected_filter_value3: "",
      percentage3: "",

      dataset3: {
        label: this.math_method3 + " of " + this.y_axis_value3,
        type: "bar",
        fill: false,
        backgroundColor: ["rgba(54, 162, 235, 0.2)"],
        borderColor: ["rgba(54, 162, 235, 1)"],
        data: ["x"],
      },

      for_datacollection: {
        labels: this.data_for_labels,
        datasets: [
          {
            label: this.math_method + " of " + this.y_axis_value,
            type: "bar",
            fill: false,
            backgroundColor: ["rgba(255, 99, 132, 0.2)"],
            borderColor: ["rgba(255, 99, 132, 1)"],
            data: ["x"],
          },
        ],
      },
      for_options: {
          scales: {
            yAxes: [
              {
                ticks: {
                  beginAtZero: true,
                },

                gridLines: {
                  display: true,
                },
              },
            ],
            xAxes: [
              {
                ticks: {
                  beginAtZero: true,
                },

                gridLines: {
                  display: true,
                },
              },
            ],
          },
          legend: {
            display: true,
          },
          responsive: true,
          maintainAspectRatio: false,
        },
      options: null,
    };
  },


  methods: {


    // ############################ FILLING DATA ################################

    fillData() {
      this.datacollection = {
        labels: this.for_datacollection.labels,
        datasets: this.for_datacollection.datasets,
      },
        this.options = this.for_options;
    },

    addDataset() {
      if (this.chart_type !== "pie" && !this.dataset2_added) {
        this.dataset2_added = true;
        this.for_datacollection.datasets.push(
          {
            label: this.math_method2 + " of " + this.y_axis_value2,
            type: "bar",
            fill: false,
            backgroundColor: ["rgba(75, 192, 192, 0.2)"],
            borderColor: ["rgba(75, 192, 192, 1)"],
            data: ["x"],
          }

        );


        this.getRandomColor();

        if (this.data_for_labels.length === 0) {
          this.for_datacollection.datasets[0]["backgroundColor"] = [
            "rgba(255, 99, 132, 0.2)",
          ];
          this.for_datacollection.datasets[0]["borderColor"] = [
            "rgba(255, 99, 132, 1)",
          ];
          this.for_datacollection.datasets[1]["backgroundColor"] = [
            "rgba(75, 192, 192, 0.2)",
          ];
          this.for_datacollection.datasets[1]["borderColor"] = [
            "rgba(75, 192, 192, 1)",
          ];
        } else {
          this.for_datacollection.datasets[0][
            "backgroundColor"
          ] = this.backgroundColor1;
          this.for_datacollection.datasets[0][
            "borderColor"
          ] = this.borderColor1;
          this.for_datacollection.datasets[1][
            "backgroundColor"
          ] = this.backgroundColor2;
          this.for_datacollection.datasets[1][
            "borderColor"
          ] = this.borderColor2;
        }
      } else if (this.chart_type !== "pie" && !this.dataset3_added) {
        this.dataset3_added = true;
        this.for_datacollection.datasets.push(
          {
            label: this.math_method3 + " of " + this.y_axis_value3,
            type: "bar",
            fill: false,
            backgroundColor: ["rgba(54, 162, 235, 0.2)"],
            borderColor: ["rgba(54, 162, 235, 1)"],
            data: ["x"]
          }

        );
        this.getRandomColor();

        if (this.data_for_labels.length === 0) {
          this.for_datacollection.datasets[0]["backgroundColor"] = [
            "rgba(255, 99, 132, 0.2)",
          ];
          this.for_datacollection.datasets[0]["borderColor"] = [
            "rgba(255, 99, 132, 1)",
          ];

          this.for_datacollection.datasets[1]["backgroundColor"] = [
            "rgba(75, 192, 192, 0.2)",
          ];
          this.for_datacollection.datasets[1]["borderColor"] = [
            "rgba(75, 192, 192, 1)",
          ];

          this.for_datacollection.datasets[2]["backgroundColor"] = [
            "rgba(54, 162, 235, 0.2)",
          ];
          this.for_datacollection.datasets[2]["borderColor"] = [
            "rgba(54, 162, 235, 1)",
          ];
        } else {
          this.for_datacollection.datasets[0][
            "backgroundColor"
          ] = this.backgroundColor1;
          this.for_datacollection.datasets[0][
            "borderColor"
          ] = this.borderColor1;
          this.for_datacollection.datasets[1][
            "backgroundColor"
          ] = this.backgroundColor2;
          this.for_datacollection.datasets[1][
            "borderColor"
          ] = this.borderColor2;
          this.for_datacollection.datasets[2][
            "backgroundColor"
          ] = this.backgroundColor3;
          this.for_datacollection.datasets[2][
            "borderColor"
          ] = this.borderColor3;
        }
      }
    },

    removeDataset() {
      if (this.dataset3_added) {
        this.dataset3_added = false;
        this.y_axis_value3 = "";
        this.data_for_datas3 = ['x'];
        this.math_method3 = 'count';
        this.chart_type3 = 'bar'
        if (this.for_datacollection.datasets.length === 3) {
          this.for_datacollection.datasets.pop();
        }
        this.dataset3 = {};
        }
        else if (this.dataset2_added) {
        this.dataset2_added = false;
        this.y_axis_value2 = "";
        this.data_for_chart2 = {};
        this.data_for_datas2 = ['x'];
        this.math_method2 = 'count';
        this.chart_type2 = 'bar'
        if (this.for_datacollection.datasets.length === 2) {
          this.for_datacollection.datasets.pop();
        }
        this.dataset2 = {};
        this.getRandomColor();
      }

      this.fillData();
    },

    //########################### GET RANDOM COLOR ##############################

    getRandomColor() {
      this.backgroundColor1 = [];
      this.borderColor1 = [];
      this.backgroundColor2 = [];
      this.borderColor2 = [];
      this.backgroundColor3 = [];
      this.borderColor3 = [];

      if (this.dataset2_added === false && this.dataset3_added === false) {
        for (var i = 0; i < this.data_for_labels.length; i++) {
          const r = Math.floor(Math.random() * 255);
          const g = Math.floor(Math.random() * 255);
          const b = Math.floor(Math.random() * 255);
          this.backgroundColor1.push(
            "rgba(" + r + ", " + g + ", " + b + ", 0.2)"
          );
          this.borderColor1.push("rgba(" + r + ", " + g + ", " + b + ", 1)");
        }
        this.for_datacollection.datasets[0][
          "backgroundColor"
        ] = this.backgroundColor1;
        this.for_datacollection.datasets[0]["borderColor"] = this.borderColor1;
      } else {
        for (var x = 0; x < this.data_for_labels.length; x++) {
          this.backgroundColor1.push("rgba(255, 99, 132, 0.2)");
          this.borderColor1.push("rgba(255, 99, 132, 1)");

          this.backgroundColor2.push("rgba(75, 192, 192, 0.2)");
          this.borderColor2.push("rgba(75, 192, 192, 1)");

          this.backgroundColor3.push("rgba(54, 162, 235, 0.2)");
          this.borderColor3.push("rgba(54, 162, 235, 1)");
        }

        this.for_datacollection.datasets[0][
          "backgroundColor"
        ] = this.backgroundColor1;
        this.for_datacollection.datasets[0]["borderColor"] = this.borderColor1;
      }
    },

    // ############################# DATA-SET-1 ##########################################3

    getXAxisValue(event) {

      this.x_axis_value = event.target.value;
      this.getNewObject();
      this.getRandomColor();

      if (
        this.y_axis_value !== "" &&
        this.math_method !== "" &&
        this.chart_type !== ""
      ) {
        this.fillData();
      }
    },

    getYAxisValue(event) {
      this.y_axis_value = event.target.value;

      this.for_datacollection.datasets[0]["label"] =
        this.math_method + " of " + this.y_axis_value;
      this.getNewObject();

      if (
        this.x_axis_value !== "" &&
        this.math_method !== "" &&
        this.chart_type !== ""
      ) {
        this.fillData();
      }
    },

    getMathMethod(event) {
      this.math_method = event.target.value;
      if (this.math_method === "average") {
        this.percentage1 = "";
      }
      this.for_datacollection.datasets[0]["label"] =
        this.math_method + " of " + this.y_axis_value;
      this.getNewObject();

      if (
        this.y_axis_value !== "" &&
        this.x_axis_value !== "" &&
        this.chart_type !== ""
      ) {
        this.fillData();
      }
    },

    getChartType(event) {
      this.chart_type = event.target.value;
      this.for_datacollection.datasets[0].type = this.chart_type;
      this.for_datacollection.datasets[0].fill = false;
      if (this.chart_type === 'pie') {
        this.for_options.scales = {};
      }
      else {
        this.for_options.scales = {
            yAxes: [
              {
                ticks: {
                  beginAtZero: true,
                },
                gridLines: {
                  display: true,
                },
              },
            ],
            xAxes: [
              {
                ticks: {
                  beginAtZero: true,
                },
                gridLines: {
                  display: true,
                },
              },
            ],
          }
      }
      

      
      if (this.chart_type === "pie") {

        if (this.for_datacollection.datasets.length === 3) {
          this.for_datacollection.datasets.pop();
          this.for_datacollection.datasets.pop();
          this.y_axis_value2 = "";
          this.data_for_chart2 = {};        
          this.data_for_datas2 = ['x'];
          this.dataset2 = {};
          this.math_method2 = 'count';
          this.chart_type2 = 'bar'
          this.y_axis_value3 = "";
          this.data_for_chart3 = {};        
          this.data_for_datas3 = [];
          this.dataset3 = {};
          this.math_method3 = 'count';
          this.chart_type3 = 'bar'
          this.dataset2_added = false;
          this.dataset3_added = false;
          this.getRandomColor()      
        } 
        else if (this.for_datacollection.datasets.length === 2) {
          this.for_datacollection.datasets.pop();
          this.y_axis_value2 = "";
          this.data_for_chart2 = {};        
          this.data_for_datas2 = [];
          this.dataset2 = {};
          this.math_method2 = 'count';
          this.chart_type2 = 'bar';
          this.dataset2_added = false;
          this.getRandomColor()
        }

      }        

        this.getNewObject();
        this.fillData();


    },

    getColumnForFilter1(event) {
      
      this.selected_filter_column1 = event.target.value;
      const set = new Set();
      this.filter_values1 = [];
      this.items.forEach((element) => {
        set.add(element[this.selected_filter_column1]);
      });
      this.filter_values1 = Array.from(set);
      this.selected_filter_value1 = '';
      if (this.selected_filter_column1 === '') {
         this.getNewObject()
        this.fillData()

      }
    },

    getValueForFilter1(event) {
      this.selected_filter_value1 = event.target.value;
      this.getNewObject();
      this.fillData();
    },

    getFilledLineChart1() {
      if (document.getElementById("filled1").checked) {
        this.for_datacollection.datasets[0].fill = true;
      } else {
        this.for_datacollection.datasets[0].fill = false;
      }
      this.fillData();
    },

    getPercentage1() {
      if (document.getElementById("percentage1").checked) {
        this.percentage1 = "percentage";
        this.for_datacollection.datasets[0]["label"] =
          this.math_method + " of " + this.y_axis_value + " (% percent)";
      } else {
        this.percentage1 = "";
        this.for_datacollection.datasets[0]["label"] =
          this.math_method + " of " + this.y_axis_value;
      }

      this.getNewObject();

      this.fillData();
    },

    getNewObject() {
      this.data_for_chart = {};
      var total_sum = 0;
      var total_count = 0;
      this.items.forEach((element) => {
        if (this.selected_filter_value1 == "") {
          if (this.data_for_chart[element[this.x_axis_value]]) {
            this.data_for_chart[element[this.x_axis_value]][0] +=
              element[this.y_axis_value];
            this.data_for_chart[element[this.x_axis_value]][1] += 1;
          } else {
            this.data_for_chart[element[this.x_axis_value]] = [
              element[this.y_axis_value],
              1,
            ];
          }

          total_sum += element[this.y_axis_value];
          total_count += 1;
        } else {
          if (
            element[this.selected_filter_column1] === this.selected_filter_value1
          ) {
            if (this.data_for_chart[element[this.x_axis_value]]) {
              this.data_for_chart[element[this.x_axis_value]][0] +=
                element[this.y_axis_value];
              this.data_for_chart[element[this.x_axis_value]][1] += 1;
            } else {
              this.data_for_chart[element[this.x_axis_value]] = [
                element[this.y_axis_value],
                1,
              ];
            }

            total_sum += element[this.y_axis_value];
            total_count += 1;
          }
        }
      });

      this.data_for_labels = Object.keys(this.data_for_chart);

      if (this.percentage1 !== "percentage") {
        if (this.math_method === "sum") {
          this.data_for_datas = Object.values(this.data_for_chart).map(
            (item) => item[0]
          );
        } else if (this.math_method === "count") {
          this.data_for_datas = Object.values(this.data_for_chart).map(
            (item) => item[1]
          );
        } else if (this.math_method === "average") {
          this.data_for_datas = Object.values(this.data_for_chart).map(
            (item) => item[0] / item[1]
          );
        }
      } else if (this.percentage1 === "percentage") {
        if (this.math_method === "sum") {
          this.data_for_datas = Object.values(this.data_for_chart).map(
            (item) => item[0] / total_sum
          );
        } else if (this.math_method === "count") {
          this.data_for_datas = Object.values(this.data_for_chart).map(
            (item) => item[1] / total_count
          );
        } else if (this.math_method === "average") {
          this.data_for_datas = Object.values(this.data_for_chart).map(
            (item) => item[0] / item[1] / (total_sum / total_count)
          );
        }
      }

      this.for_datacollection.labels = this.data_for_labels;

      this.for_datacollection.datasets[0].data = this.data_for_datas;

    },

    // ############################# DATA-SET-2 ##########################################3

    getYAxisValue2(event) {
      this.y_axis_value2 = event.target.value;
      this.for_datacollection.datasets[1]["label"] =
        this.math_method2 + " of " + this.y_axis_value2;
      this.getNewObject2();
      this.fillData();

    },

    getMathMethod2(event) {
      this.math_method2 = event.target.value;
      if (this.math_method2 === "average") {
        this.percentage2 = "";
      }
      this.for_datacollection.datasets[1]["label"] =
        this.math_method2 + " of " + this.y_axis_value2;
      this.getNewObject2();
      this.fillData();
    },

    getChartType2(event) {
      this.chart_type2 = event.target.value;
      this.for_datacollection.datasets[1].type = this.chart_type2;
      this.for_datacollection.datasets[1].fill = false;
      this.fillData();
      

    },

    getColumnForFilter2(event) {
      this.selected_filter_column2 = event.target.value;
      const set = new Set();
      this.filter_values2 = [];
      this.items.forEach((element) => {
        set.add(element[this.selected_filter_column2]);
      });

      this.filter_values2 = Array.from(set);
      this.selected_filter_value2 = '';
      if (this.selected_filter_column2 === '') {
         this.getNewObject2()
        this.fillData()

      }
    },

    getValueForFilter2(event) {
      this.selected_filter_value2 = event.target.value;

      this.getNewObject2();
      this.fillData();
    },

    getFilledLineChart2() {
      if (document.getElementById("filled2").checked) {
        this.for_datacollection.datasets[1].fill = true;
      } else {
        this.for_datacollection.datasets[1].fill = false;
      }

      this.fillData();
    },

    getPercentage2() {
      if (document.getElementById("percentage2").checked) {
        this.percentage2 = "percentage";
        this.for_datacollection.datasets[1]["label"] = this.math_method2 + " of " + this.y_axis_value2 + " (% percent)";
      } else {
        this.percentage2 = "";
        this.for_datacollection.datasets[1]["label"] = this.math_method2 + " of " + this.y_axis_value2;
      }
      this.getNewObject2();
      this.fillData();
    },

    getNewObject2() {
      this.data_for_chart2 = {};
      var total_sum = 0;
      var total_count = 0;
      this.items.forEach((element) => {
        if (this.selected_filter_value1 == "") {
          if (this.data_for_chart2[element[this.x_axis_value]]) {
            this.data_for_chart2[element[this.x_axis_value]][0] +=
              element[this.y_axis_value2];
            this.data_for_chart2[element[this.x_axis_value]][1] += 1;
          } else {
            this.data_for_chart2[element[this.x_axis_value]] = [
              element[this.y_axis_value2],
              1,
            ];
          }

          total_sum += element[this.y_axis_value2];
          total_count += 1;
        } else {
          if (
            element[this.selected_filter_column2] ===
            this.selected_filter_value2
          ) {
            if (this.data_for_chart2[element[this.x_axis_value]]) {
              this.data_for_chart2[element[this.x_axis_value]][0] +=
                element[this.y_axis_value2];
              this.data_for_chart2[element[this.x_axis_value]][1] += 1;
            } else {
              this.data_for_chart2[element[this.x_axis_value]] = [
                element[this.y_axis_value2],
                1,
              ];
            }
          }

          total_sum += element[this.y_axis_value2];
          total_count += 1;
        }
      });

      if (this.percentage2 !== "percentage") {
        if (this.math_method2 === "sum") {
          this.data_for_datas2 = Object.values(this.data_for_chart2).map(
            (item) => item[0]
          );
        } else if (this.math_method2 === "count") {
          this.data_for_datas2 = Object.values(this.data_for_chart2).map(
            (item) => item[1]
          );
        } else if (this.math_method2 === "average") {
          this.data_for_datas2 = Object.values(this.data_for_chart2).map(
            (item) => item[0] / item[1]
          );
        }
      } else if (this.percentage2 === "percentage") {
        if (this.math_method2 === "sum") {
          this.data_for_datas2 = Object.values(this.data_for_chart2).map(
            (item) => item[0] / total_sum
          );
        } else if (this.math_method2 === "count") {
          this.data_for_datas2 = Object.values(this.data_for_chart2).map(
            (item) => item[1] / total_count
          );
        } else if (this.math_method2 === "average") {
          this.data_for_datas2 = Object.values(this.data_for_chart2).map(
            (item) => item[0] / item[1] / (total_sum / total_count)
          );
        }
      }

      this.for_datacollection.datasets[1].data = this.data_for_datas2;

      this.for_datacollection.datasets[1]["backgroundColor"] = this.backgroundColor2;
      this.for_datacollection.datasets[1]["borderColor"] = this.borderColor2;
    },

    // ############################# DATA-SET-3 ##########################################3

    getYAxisValue3(event) {
      this.y_axis_value3 = event.target.value;
      this.for_datacollection.datasets[2]["label"] =
        this.math_method3 + " of " + this.y_axis_value3;

      this.getNewObject3();

      this.fillData();
    },

    getMathMethod3(event) {
      this.math_method3 = event.target.value;

      if (this.math_method3 === "average") {
        this.percentage3 = "";
      }

      this.for_datacollection.datasets[2]["label"] =
        this.math_method3 + " of " + this.y_axis_value3;

      this.getNewObject3();
      this.fillData();
    },

    getChartType3(event) {
      this.chart_type3 = event.target.value;
      this.for_datacollection.datasets[2].type = this.chart_type3;
      this.for_datacollection.datasets[2].fill = false;
      this.fillData();
    },

    getColumnForFilter3(event) {
      this.selected_filter_column3 = event.target.value;
      const set = new Set();
      this.filter_values3 = [];
      this.items.forEach((element) => {
        set.add(element[this.selected_filter_column3]);
      });

      this.filter_values3 = Array.from(set);
      this.selected_filter_value3 = '';
      if (this.selected_filter_column3 === '') {
        this.getNewObject3()
        this.fillData()

      }
    },

    getValueForFilter3(event) {
      this.selected_filter_value3 = event.target.value;

      this.getNewObject3();
      this.fillData();
    },

    getFilledLineChart3() {
      if (document.getElementById("filled3").checked) {
        this.for_datacollection.datasets[2].fill = true;
      } else {
        this.for_datacollection.datasets[2].fill = false;
      }

      this.fillData();
    },

    getPercentage3() {
      if (document.getElementById("percentage3").checked) {
        this.percentage3 = "percentage";
        this.for_datacollection.datasets[2]["label"] =
          this.math_method3 + " of " + this.y_axis_value3 + " (% percent)";
      } else {
        this.percentage3 = "";
        this.for_datacollection.datasets[2]["label"] =
          this.math_method3 + " of " + this.y_axis_value3 + " (% percent)";
      }
      this.getNewObject3();
      this.fillData();
    },

    getNewObject3() {
      this.data_for_chart3 = {};
      var total_sum = 0;
      var total_count = 0;
      this.items.forEach((element) => {
        if (this.selected_filter_value3 == "") {
          if (this.data_for_chart3[element[this.x_axis_value]]) {
            this.data_for_chart3[element[this.x_axis_value]][0] +=
              element[this.y_axis_value3];
            this.data_for_chart3[element[this.x_axis_value]][1] += 1;
          } else {
            this.data_for_chart3[element[this.x_axis_value]] = [
              element[this.y_axis_value3],
              1,
            ];
          }

          total_sum += element[this.y_axis_value3];
          total_count += 1;
        } else {
          if (
            element[this.selected_filter_column3] ===
            this.selected_filter_value3
          ) {
            if (this.data_for_chart3[element[this.x_axis_value]]) {
              this.data_for_chart3[element[this.x_axis_value]][0] +=
                element[this.y_axis_value3];
              this.data_for_chart3[element[this.x_axis_value]][1] += 1;
            } else {
              this.data_for_chart3[element[this.x_axis_value]] = [
                element[this.y_axis_value3],
                1,
              ];
            }

            total_sum += element[this.y_axis_value3];
            total_count += 1;
          }
        }
      });

      if (this.percentage3 !== "percentage") {
        if (this.math_method3 === "sum") {
          this.data_for_datas3 = Object.values(this.data_for_chart3).map(
            (item) => item[0]
          );
        } else if (this.math_method3 === "count") {
          this.data_for_datas3 = Object.values(this.data_for_chart3).map(
            (item) => item[1]
          );
        } else if (this.math_method3 === "average") {
          this.data_for_datas3 = Object.values(this.data_for_chart3).map(
            (item) => item[0] / item[1]
          );
        }
      } else if (this.percentage3 === "percentage") {
        if (this.math_method3 === "sum") {
          this.data_for_datas3 = Object.values(this.data_for_chart3).map(
            (item) => item[0] / total_sum
          );
        } else if (this.math_method3 === "count") {
          this.data_for_datas3 = Object.values(this.data_for_chart3).map(
            (item) => item[1] / total_count
          );
        } else if (this.math_method3 === "average") {
          this.data_for_datas3 = Object.values(this.data_for_chart3).map(
            (item) => item[0] / item[1] / (total_sum / total_count)
          );
        }
      }

      this.for_datacollection.datasets[2].data = this.data_for_datas3;

      this.for_datacollection.datasets[2][
        "backgroundColor"
      ] = this.backgroundColor3;
      this.for_datacollection.datasets[2]["borderColor"] = this.borderColor3;
    },
  },
};
</script>

<style>
.small {
  max-width: 600px;
  margin: 150px auto;
}

td {
  font-size: 12px;
}

td {
  padding: 2px 5px;
}

tr.criteria {
  background: linear-gradient(to bottom, #fff899 0%, #99b1ff 100%);
}

button {
  background-color: dodgerblue;
  color: white;
  font-weight: bold;
  border-radius: 5px;
}

select {
  background: linear-gradient(to bottom, #66ccff 0%, #ffccff 100%);
  border-radius: 5px;
}
</style>
