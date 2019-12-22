<template>
  <div class="home">
    <div class="chart-container">
      <charts :data="chartData" />
    </div>
    <div class="slider">
      <div class="slider-box">
        <Slider
        @on-change="indexChange"
        :min="0"
        :max="390"
        v-model="dataIndex"></Slider>
      </div>
    </div>
  </div>
</template>

<script>
// @ is an alias to /src
import axios from 'axios';
import charts from '@/components/charts.vue';

export default {
  name: 'home',
  components: {
    charts,
  },
  data() {
    return {
      chartData: {
        xList: [],
        yList: [],
        date: '',
      },
      dataList: [],
      dataIndex: 0,
    };
  },
  mounted() {
    axios.get('http://localhost:8080/static/data.json').then((res) => {
      const { dataList } = res.data;
      this.dataList = dataList;
      this.indexChange(0);
      console.log(this.chartData);
    });
  },
  methods: {
    indexChange(val) {
      this.chartData.xList = this.dataList[val].xList;
      this.chartData.yList = this.dataList[val].yList;
      this.chartData.date = this.dataList[val].date;
    },
  },
};
</script>
<style lang="less" scoped>
  .chart-container{
    display: flex;
    justify-content: center;
  }
  .slider{
    margin-top: 20px;
    display: flex;
    justify-content: center;
    .slider-box{
      width: 800px;
    }
  }
</style>
