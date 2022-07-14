console.log("rs");
try {
	Apex.tooltip = {
		theme: "dark",
	};

	/*
      ==============================
      |    @Options Charts Script   |
      ==============================
  */

	/*
      ======================================
          Visitor Statistics | Options
      ======================================
  */

	// Total Visits

	var spark1 = {
		chart: {
			id: "unique-visits",
			group: "sparks2",
			type: "line",
			height: 80,
			sparkline: {
				enabled: true,
			},
			dropShadow: {
				enabled: true,
				top: 1,
				left: 1,
				blur: 2,
				color: "#e2a03f",
				opacity: 0.7,
			},
		},
		series: [
			{
				data: [21, 9, 36, 12, 44, 25, 59, 41, 66, 25],
			},
		],
		stroke: {
			curve: "smooth",
			width: 2,
		},
		markers: {
			size: 0,
		},
		grid: {
			padding: {
				top: 35,
				bottom: 0,
				left: 40,
			},
		},
		colors: ["#e2a03f"],
		tooltip: {
			x: {
				show: false,
			},
			y: {
				title: {
					formatter: function formatter(val) {
						return "";
					},
				},
			},
		},
		responsive: [
			{
				breakpoint: 1351,
				options: {
					chart: {
						height: 95,
					},
					grid: {
						padding: {
							top: 35,
							bottom: 0,
							left: 0,
						},
					},
				},
			},
			{
				breakpoint: 1200,
				options: {
					chart: {
						height: 80,
					},
					grid: {
						padding: {
							top: 35,
							bottom: 0,
							left: 40,
						},
					},
				},
			},
			{
				breakpoint: 576,
				options: {
					chart: {
						height: 95,
					},
					grid: {
						padding: {
							top: 45,
							bottom: 0,
							left: 0,
						},
					},
				},
			},
		],
	};

	// Paid Visits

	var spark2 = {
		chart: {
			id: "total-users",
			group: "sparks1",
			type: "line",
			height: 80,
			sparkline: {
				enabled: true,
			},
			dropShadow: {
				enabled: true,
				top: 3,
				left: 1,
				blur: 3,
				color: "#009688",
				opacity: 0.7,
			},
		},
		series: [
			{
				data: [22, 19, 30, 47, 32, 44, 34, 55, 41, 69],
			},
		],
		stroke: {
			curve: "smooth",
			width: 2,
		},
		markers: {
			size: 0,
		},
		grid: {
			padding: {
				top: 35,
				bottom: 0,
				left: 40,
			},
		},
		colors: ["#009688"],
		tooltip: {
			x: {
				show: false,
			},
			y: {
				title: {
					formatter: function formatter(val) {
						return "";
					},
				},
			},
		},
		responsive: [
			{
				breakpoint: 1351,
				options: {
					chart: {
						height: 95,
					},
					grid: {
						padding: {
							top: 35,
							bottom: 0,
							left: 0,
						},
					},
				},
			},
			{
				breakpoint: 1200,
				options: {
					chart: {
						height: 80,
					},
					grid: {
						padding: {
							top: 35,
							bottom: 0,
							left: 40,
						},
					},
				},
			},
			{
				breakpoint: 576,
				options: {
					chart: {
						height: 95,
					},
					grid: {
						padding: {
							top: 35,
							bottom: 0,
							left: 0,
						},
					},
				},
			},
		],
	};

	/*
      ===================================
          Unique Visitors | Options
      ===================================
  */

	var d_1options1 = {
		chart: {
			height: 350,
			type: "bar",
			toolbar: {
				show: false,
			},
			dropShadow: {
				enabled: true,
				top: 1,
				left: 1,
				blur: 1,
				color: "#515365",
				opacity: 0.3,
			},
		},
		colors: ["#5c1ac3", "#ffbb44"],
		plotOptions: {
			bar: {
				horizontal: false,
				columnWidth: "55%",
				endingShape: "rounded",
			},
		},
		dataLabels: {
			enabled: false,
		},
		legend: {
			position: "bottom",
			horizontalAlign: "center",
			fontSize: "14px",
			markers: {
				width: 10,
				height: 10,
			},
			itemMargin: {
				horizontal: 0,
				vertical: 8,
			},
		},
		grid: {
			borderColor: "#191e3a",
		},
		stroke: {
			show: true,
			width: 2,
			colors: ["transparent"],
		},
		series: [
			{
				name: "Direct",
				data: [58, 44, 55, 57, 56, 61, 58, 63, 60, 66, 56, 63],
			},
			{
				name: "Organic",
				data: [91, 76, 85, 101, 98, 87, 105, 91, 114, 94, 66, 70],
			},
		],
		xaxis: {
			categories: [
				"Jan",
				"Feb",
				"Mar",
				"Apr",
				"May",
				"Jun",
				"Jul",
				"Aug",
				"Sep",
				"Oct",
				"Nov",
				"Dec",
			],
		},
		fill: {
			type: "gradient",
			gradient: {
				shade: "dark",
				type: "vertical",
				shadeIntensity: 0.3,
				inverseColors: false,
				opacityFrom: 1,
				opacityTo: 0.8,
				stops: [0, 100],
			},
		},
		tooltip: {
			theme: "dark",
			y: {
				formatter: function (val) {
					return val;
				},
			},
		},
	};

	/*
      ==============================
          Statistics | Options
      ==============================
  */

	// Followers

	var d_1options3 = {
		chart: {
			id: "sparkline1",
			type: "area",
			height: 160,
			sparkline: {
				enabled: true,
			},
		},
		stroke: {
			curve: "smooth",
			width: 2,
		},
		series: [
			{
				name: "Sales",
				data: [38, 60, 38, 52, 36, 40, 28],
			},
		],
		labels: ["1", "2", "3", "4", "5", "6", "7"],
		yaxis: {
			min: 0,
		},
		colors: ["#4361ee"],
		tooltip: {
			x: {
				show: false,
			},
		},
		fill: {
			type: "gradient",
			gradient: {
				type: "vertical",
				shadeIntensity: 1,
				inverseColors: !1,
				opacityFrom: 0.3,
				opacityTo: 0.05,
				stops: [100, 100],
			},
		},
	};

	// Referral

	var d_1options4 = {
		chart: {
			id: "sparkline1",
			type: "area",
			height: 160,
			sparkline: {
				enabled: true,
			},
		},
		stroke: {
			curve: "smooth",
			width: 2,
		},
		series: [
			{
				name: "Sales",
				data: [60, 28, 52, 38, 40, 36, 38],
			},
		],
		labels: ["1", "2", "3", "4", "5", "6", "7"],
		yaxis: {
			min: 0,
		},
		colors: ["#e7515a"],
		tooltip: {
			x: {
				show: false,
			},
		},
		fill: {
			type: "gradient",
			gradient: {
				type: "vertical",
				shadeIntensity: 1,
				inverseColors: !1,
				opacityFrom: 0.3,
				opacityTo: 0.05,
				stops: [100, 100],
			},
		},
	};

	// Engagement Rate

	var d_1options5 = {
		chart: {
			id: "sparkline1",
			type: "area",
			height: 160,
			sparkline: {
				enabled: true,
			},
		},
		stroke: {
			curve: "smooth",
			width: 2,
		},
		fill: {
			opacity: 1,
		},
		series: [
			{
				name: "Sales",
				data: [28, 50, 36, 60, 38, 52, 38],
			},
		],
		labels: ["1", "2", "3", "4", "5", "6", "7"],
		yaxis: {
			min: 0,
		},
		colors: ["#1abc9c"],
		tooltip: {
			x: {
				show: false,
			},
		},
		fill: {
			type: "gradient",
			gradient: {
				type: "vertical",
				shadeIntensity: 1,
				inverseColors: !1,
				opacityFrom: 0.3,
				opacityTo: 0.05,
				stops: [100, 100],
			},
		},
	};

	const base_donut_options = {
		chart: {
			type: "donut",
			width: 400,
		},
		colors: ["#5c1ac3", "#e2a03f", "#e7515a", "#1abc9c", "#e0e6ed"],
		dataLabels: {
			enabled: false,
		},
		legend: {
			position: "bottom",
			horizontalAlign: "center",
			fontSize: "14px",
			markers: {
				width: 10,
				height: 10,
			},
			itemMargin: {
				horizontal: 0,
				vertical: 8,
			},
		},
		plotOptions: {
			pie: {
				donut: {
					size: "65%",
					background: "transparent",
					labels: {
						show: true,
						name: {
							show: true,
							fontSize: "29px",
							fontFamily: "Nunito, sans-serif",
							color: undefined,
							offsetY: -10,
						},
						value: {
							show: true,
							fontSize: "26px",
							fontFamily: "Nunito, sans-serif",
							color: "#bfc9d4",
							offsetY: 16,
							formatter: function (val) {
								return val + "%";
							},
						},
						total: {
							show: true,
							showAlways: true,
							label: "Total",
							color: "#888ea8",
							// formatter: function (w) {
							// 	return w.globals.seriesTotals.reduce(function (a, b) {
							// 		return a + b;
							// 	}, 0) + '%';
							// },
							formatter: function () {
								return "100%";
							},
						},
					},
				},
			},
		},
		stroke: {
			show: true,
			width: 5,
			colors: "#0e1726",
		},
		series: [985, 737, 270],
		labels: ["Apparel", "Sports", "Others"],
	};

	/*
      ==============================
      |    @Render Charts Script    |
      ==============================
  */

	/*
      ======================================
          Visitor Statistics | Script
      ======================================
  */

	// Total Visits
	d_1C_1 = new ApexCharts(document.querySelector("#total-users"), spark1);
	d_1C_1.render();

	// Paid Visits
	d_1C_2 = new ApexCharts(document.querySelector("#paid-visits"), spark2);
	d_1C_2.render();

	// labeled_TB chart
	(async () => {
		const q = getQueryParamValueByKey("q") || "";
		const limit = getQueryParamValueByKey("limit") || 100;
		const analysis = getQueryParamValueByKey("analysis") || "textblob";
		const lang = getQueryParamValueByKey("lang") || "en";
		const load_screen = document.querySelector(".charts-loader");
		const charts_wrapper = document.querySelector(".home-charts-wrapper");

		charts_wrapper.style.display = "none";

		const fetch_data = await fetch(
			`/home/home_data?q=${q}&limit=${limit}&analysis=${analysis}&lang=${lang}`
		).then((res) => res.json());

		charts_wrapper.style.display = "flex";
		load_screen.style.display = "none";

		// word cloud
		WordCloud(document.getElementById("word-cloud"), {
			list: fetch_data?.counts_sorted || [],
			gridSize: Math.round((16 * $("#word-cloud").width()) / 1024),
			weightFactor: function (size) {
				return size * 4;
				// return (Math.pow(size, 2.3) * $("#word-cloud").width()) / 1024;
			},
			fontFamily: "Times, serif",
			color: "#e2a03f",
			rotateRatio: 0.5,
			rotationSteps: 2,
			backgroundColor: "#0e1726",
			// shape: () => {
			// 	// TODO : https://wordcloud2-js.timdream.org/index.js
			// }
		});

		// stats
		if (fetch_data?.stats) {
			var old_date = moment(fetch_data?.stats?.newest_tweet_date);
			var new_date = moment(fetch_data?.stats?.oldest_tweet_date);
			var diff = old_date.diff(new_date, "days") || 1;

			document.querySelector(
				".time-span-state .w-content .value"
			).innerHTML = `${diff}`;

			[
				"number_of_replies",
				"number_of_retweets",
				"number_of_tweets",
				"numbers_of_languages",
				"number_of_likes",
			].forEach((el) => {
				const key = el.split("_")[el.split("_").length - 1];
				const val = fetch_data?.stats?.[el] || 0;

				// setTimeout(() => {
				// 	window.CountUp && new window.CountUp(`${el}_counter`, val).start();
				// }, 1000)

				document.querySelector(
					`.${el} .w-content .value`
				).innerHTML = `${val}`;
			});

			// tweets sample
			const good_tweet = parseJSONstring(fetch_data?.random_good_sample)[0];
			const good_tweet_wrapper = document.querySelector(".good-tweet-wrapper");
			good_tweet_wrapper.querySelector(
				".tweet-header img"
			).src = `https://robohash.org/${good_tweet?.username}?set=set3`;
			good_tweet_wrapper.querySelector(".tweet-header-info").innerHTML = `
				${good_tweet?.username} <span>@${good_tweet?.username}</span>
				<span>${good_tweet?.date?.split(' ')[0]}</span>
				<p>
					${good_tweet?.tweet}
				</p>
			`;
			good_tweet_wrapper.querySelector(".tweet-info-counts .likes-count").textContent = `${good_tweet?.nlikes}`;
			good_tweet_wrapper.querySelector(".tweet-info-counts .comment-count").textContent = `${good_tweet?.nreplies}`;
			good_tweet_wrapper.querySelector(".tweet-info-counts .retweet-count").textContent = `${good_tweet?.nretweets}`;

			const bad_tweet = parseJSONstring(fetch_data?.random_bad_sample)[0];
			const bad_tweet_wrapper = document.querySelector(".bad-tweet-wrapper");
			bad_tweet_wrapper.querySelector(
				".tweet-header img"
			).src = `https://robohash.org/${bad_tweet?.username}?set=set3`;
			bad_tweet_wrapper.querySelector(".tweet-header-info").innerHTML = `
				${bad_tweet?.username} <span>@${bad_tweet?.username}</span>
				<span>${bad_tweet?.date?.split(' ')[0]}</span>
				<p>
					${bad_tweet?.tweet}
				</p>
			`;
			bad_tweet_wrapper.querySelector(".tweet-info-counts .likes-count").textContent = `${bad_tweet?.nlikes}`;
			bad_tweet_wrapper.querySelector(".tweet-info-counts .comment-count").textContent = `${bad_tweet?.nreplies}`;
			bad_tweet_wrapper.querySelector(".tweet-info-counts .retweet-count").textContent = `${bad_tweet?.nretweets}`;
		}

		if (fetch_data?.analysis_type === "textblob") {
			labeled_TB_chart = new ApexCharts(document.querySelector("#labeled-tb"), {
				...base_donut_options,
				series: Object.values(fetch_data?.analysis_data),
				labels: Object.keys(fetch_data?.analysis_data),
			});
			labeled_TB_chart.render();
			document.querySelector(".analysis_type_textblob").style.display = "block";
		} else if (fetch_data?.analysis_type === "camelbert") {
			labeled_cml_chart = new ApexCharts(
				document.querySelector("#labeled-cml"),
				{
					...base_donut_options,
					series: Object.values(fetch_data?.analysis_data),
					labels: Object.keys(fetch_data?.analysis_data),
				}
			);
			labeled_cml_chart.render();
			document.querySelector(".analysis_type_camel").style.display = "block";
		} else if (fetch_data?.analysis_type === "bert") {
			labeled_bert_chart = new ApexCharts(
				document.querySelector("#labeled-bert"),
				{
					...base_donut_options,
					series: Object.values(fetch_data?.analysis_data),
					labels: Object.keys(fetch_data?.analysis_data),
				}
			);
			labeled_bert_chart.render();
			document.querySelector(".analysis_type_bert").style.display = "block";
		}
	})();

	/*
      ===================================
          Unique Visitors | Script
      ===================================
  */

	var d_1C_3 = new ApexCharts(
		document.querySelector("#uniqueVisits"),
		d_1options1
	);
	d_1C_3.render();

	/*
      ==============================
          Statistics | Script
      ==============================
  */

	// Followers

	var d_1C_5 = new ApexCharts(
		document.querySelector("#hybrid_followers"),
		d_1options3
	);
	d_1C_5.render();

	// Referral

	var d_1C_6 = new ApexCharts(
		document.querySelector("#hybrid_followers1"),
		d_1options4
	);
	d_1C_6.render();

	// Engagement Rate

	var d_1C_7 = new ApexCharts(
		document.querySelector("#hybrid_followers3"),
		d_1options5
	);
	d_1C_7.render();

	/*
    =============================================
        Perfect Scrollbar | Notifications
    =============================================
*/
	const ps = new PerfectScrollbar(document.querySelector(".mt-container"));
} catch (e) {
	// statements
	console.log(e);
}

// utils
function getQueryParamValueByKey(key) {
	var url = window.location.href;
	key = key.replace(/[\[\]]/g, "\\$&");
	var regex = new RegExp("[?&]" + key + "(=([^&#]*)|&|#|$)"),
		results = regex.exec(url);
	if (!results) return null;
	if (!results[2]) return "";
	return decodeURIComponent(results[2].replace(/\+/g, " "));
}

function parseJSONstring(str) {
	return JSON.parse(str.replace('\\"', '"')) || {};
}
