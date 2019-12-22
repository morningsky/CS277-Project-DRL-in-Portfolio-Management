<template>
  <div :id="randomId" style="width:1000px;height:400px;margin: 0 auto;" />
</template>
<script>
import echarts from 'echarts';

export default {
  props: {
    data: {
      type: Object,
    },
  },
  data() {
    return {
      chart: null,
      randomId: `echart${Math.floor(Math.random() * 10000)}`,
    };
  },
  watch: {
    data: {
      handler() {
        this.initChart();
      },
      deep: true,
    },
  },
  mounted() {
    this.initChart();
  },
  methods: {
    initChart() {
      const newVal = this.data;
      this.chart = echarts.init(document.getElementById(this.randomId));
      this.chart.setOption({
        title: {
          text: newVal.date,
          x: 'center',
          y: 'bottom',
          textAlign: 'left',
        },
        xAxis: {
          type: 'category',
          data: newVal.xList,
        },
        yAxis: {
          type: 'value',
        },
        series: [{
          data: newVal.yList,
          type: 'bar',
        }],
      });
    },
  },
};
</script>
