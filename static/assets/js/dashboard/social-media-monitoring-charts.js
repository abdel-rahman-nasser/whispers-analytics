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
				name: "Follower",
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
				name: "Following",
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
				name: "Posts",
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
							formatter: function (w) {
								return (
									w.globals.seriesTotals.reduce(function (a, b) {
										return a + b;
									}, 0) + "%"
								);
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

	/*
      ==============================
          Statistics | Script
      ==============================
  */

	// Followers

	(async () => {
		const social_media_monitoring_charts_wrapper = document.querySelector('.social-media-monitoring-charts-wrapper')
		const charts_loader = document.querySelector('.charts-loader')

		// helpers
		const response_data_formatter = (response_string) => {
			try {
				return JSON.parse(response_string.replace('"', '"').replace("/", "/"));
			} catch (err) {
				return {};
			}
		};
		const nFormatter = function (num, digits = 1) {
			const lookup = [
				{ value: 1, symbol: "" },
				{ value: 1e3, symbol: "k" },
				{ value: 1e6, symbol: "M" },
				{ value: 1e9, symbol: "G" },
				{ value: 1e12, symbol: "T" },
				{ value: 1e15, symbol: "P" },
				{ value: 1e18, symbol: "E" },
			];
			const rx = /\.0+$|(\.[0-9]*[1-9])0+$/;
			var item = lookup
				.slice()
				.reverse()
				.find(function (item) {
					return num >= item.value;
				});
			return item
				? (num / item.value).toFixed(digits).replace(rx, "$1") + item.symbol
				: "0";
		};

		// get all platforms data from the api
		const [instagram_res, facebook_res, twitter_res, user_details_res] = await Promise.all([
			fetch("/social_media_monitoring/instagram_data").then((res) =>
				res.json()
			),
			fetch("/social_media_monitoring/facebook_data").then((res) => res.json()),
			fetch("/social_media_monitoring/twitter_data").then((res) => res.json()),
			fetch("/social_media_monitoring/user_details").then((res) => res.json()),
		]);

		const { instagram_page_info, instagram_page_posts } = {
			instagram_page_info: response_data_formatter(
				instagram_res.instagram_page_info
			)[0],
			instagram_page_posts: response_data_formatter(
				instagram_res.instagram_page_posts
			),
		};

		const { facebook_page_info, facebook_page_posts } = {
			facebook_page_info: facebook_res.facebook_page_info,
			facebook_page_posts: response_data_formatter(
				facebook_res.facebook_page_posts
			),
		};

		const { twitter_user_info, twitter_user_data } = {
			twitter_user_info: response_data_formatter(
				twitter_res.twitter_user_info
			)[0],
			twitter_user_data: response_data_formatter(twitter_res.twitter_user_data),
		};

		// set followers
		const total_of_follower =
			instagram_page_info.number_of_followers +
			facebook_page_info.pg_follows +
			twitter_user_info.followers_num;
		document.querySelector(".widget-followers .w-value").textContent =
			nFormatter(total_of_follower);

		// set following
		const total_of_following = instagram_page_info.number_of_followings;
		document.querySelector(".widget-referral .w-value").textContent =
			nFormatter(total_of_following);

		// numbers of posts
		const numbers_of_posts =
			instagram_page_info.number_of_posts + twitter_user_info.tweets_num;
		document.querySelector(".widget-engagement .w-value").textContent =
			nFormatter(numbers_of_posts);

		// calc the percentage of follower per platform rounded to 2 decimal places
		const instagram_follower_percentage = Math.round(
			(instagram_page_info.number_of_followers / total_of_follower) * 100
		);
		const facebook_follower_percentage = Math.round(
			(facebook_page_info.pg_follows / total_of_follower) * 100
		);
		const twitter_follower_percentage = Math.round(
			(twitter_user_info.followers_num / total_of_follower) * 100
		);

		// sort platforms by followers
		const platforms_by_followers = [
			{
				name: "Instagram",
				cls: ".insta-stat",
				followers: instagram_page_info.number_of_followers,
				percentage: instagram_follower_percentage,
			},
			{
				name: "Facebook",
				cls: ".fb-stat",
				followers: facebook_page_info.pg_follows,
				percentage: facebook_follower_percentage,
			},
			{
				name: "Twitter",
				cls: ".twitter-stat",
				followers: twitter_user_info.followers_num,
				percentage: twitter_follower_percentage,
			},
		];
		platforms_by_followers.sort((a, b) => {
			return b.followers - a.followers;
		});

		// sort dom elements according to the platforms by followers
		platforms_by_followers.forEach((platform) => {
			const el = document.querySelector(platform.cls).cloneNode(true);
			document.querySelector(".vistorsBrowser").appendChild(el);
		});

		document
			.querySelectorAll(".vistorsBrowser .browser-list")
			.forEach((el, i) => {
				if (i <= 2) {
					el.remove();
				}
			});

		// populate the dom
		document.querySelector(
			".facebook-followers-percentage"
		).textContent = `${facebook_follower_percentage}%`;
		document.querySelector(
			".facebook-followers-progressbar"
		).style.width = `${facebook_follower_percentage}%`;
		document.querySelector(
			".instagram-followers-percentage"
		).textContent = `${instagram_follower_percentage}%`;
		document.querySelector(
			".instagram-followers-progressbar"
		).style.width = `${instagram_follower_percentage}%`;
		document.querySelector(
			".twitter-followers-percentage"
		).textContent = `${twitter_follower_percentage}%`;
		document.querySelector(
			".twitter-followers-progressbar"
		).style.width = `${twitter_follower_percentage}%`;

		// set engagement_rate
		const engagement_rate = (
			instagram_res.engagement_rate
		).toFixed(2);
		
		document.querySelector(
			".meter-container h1"
		).textContent = `${engagement_rate}%`;
		const label_el = document.querySelector(".meter-container .meter-label");
		const meter_title = document.querySelector(".meter-container h1");

		if (engagement_rate < 33.33) {
			label_el.classList.add("danger");
			label_el.textContent = "Low Engagement";
			// meter_title.textContent = 'Low Engagement'
			meter_title.classList.add('danger');
		} else if (engagement_rate < 66.66) {
			label_el.classList.add("warning");
			label_el.textContent = "Medium Engagement";
			// meter_title.textContent = 'Medium Engagement'
			meter_title.classList.add('warning');
		} else {
			label_el.classList.add("success");
			label_el.textContent = "High Engagement :D";
			// meter_title.textContent = 'High Engagement :D'
			meter_title.classList.add('success');
		}

		// get formatted date from timestamp util function
		const timestampToDate = (timestamp) => {
			const date = new Date(timestamp * 1000);
			// const date_string = date.toLocaleDateString();
			return date;
		};

		const month_names = [
			"January",
			"February",
			"March",
			"April",
			"May",
			"June",
			"July",
			"August",
			"September",
			"October",
			"November",
			"December",
		];

		const getMothFromDate = (date) => {
			const month = date.getMonth();
			return month_names[month];
		};

		const formatted_fb_data = facebook_page_posts.map((post) => {
			const formatted_post_date = timestampToDate(post.upload_date);
			return {
				date: formatted_post_date,
				month: getMothFromDate(formatted_post_date),
				likes: post["Total_Reacts"] || 0,
				comments: post["Num_Comments"] || 0,
				shares: post["Num_Shares"] || 0,
				content: post['Content'] || '',
				image: '',
				source: 'facebook',
			};
		});

		const formatted_insta_data = instagram_page_posts.map((post) => {
			const formatted_post_date = timestampToDate(post.date_utc);
			return {
				date: formatted_post_date,
				month: getMothFromDate(formatted_post_date),
				likes: post["Likes"] || 0,
				comments: post["Num_Comments"] || 0,
				shares: 0,
				content: post['caption'] || '',
				image: post['post_url'] || '',
				source: 'instagram',
			};
		});

		const formatted_twt_data = twitter_user_data.map((post) => {
			const formatted_post_date = new Date(post.date);
			return {
				date: formatted_post_date,
				month: getMothFromDate(formatted_post_date),
				likes: post["nlikes"] || 0,
				comments: post["nreplies"] || 0,
				shares: post["nretweets"] || 0,
				content: post['tweet'] || '',
				image: '',
				source: 'twitter',
			};
		});

		// sub of likes per month in all platforms
		const merged_formatted_data = [
			...formatted_fb_data,
			...formatted_insta_data,
			...formatted_twt_data,
		];

		// totals
		const total_likes = merged_formatted_data.reduce(
			(acc, curr) => acc + curr.likes,
			0
		);
		const total_comments = merged_formatted_data.reduce(
			(acc, curr) => acc + curr.comments,
			0
		);
		const total_shares = merged_formatted_data.reduce(
			(acc, curr) => acc + curr.shares,
			0
		);
		const top_month_per_likes = merged_formatted_data.reduce(
			(acc, curr) => {
				if (curr.likes > acc.likes) {
					return {
						month: curr.month,
						likes: curr.likes,
					};
				}
				return acc;
			},
			{ month: "", likes: 0 }
		);
		const get_day_of_the_week_by_name = (index) => {
			const day_names = [
				"Sunday",
				"Monday",
				"Tuesday",
				"Wednesday",
				"Thursday",
				"Friday",
				"Saturday",
			];
			return day_names[index];
		}

		const top_day_of_the_week_per_likes = merged_formatted_data.reduce(
			(acc, curr) => {
				if (curr.likes > acc.likes) {
					return {
						day: curr.date.getDay(),
						likes: curr.likes,
					};
				}
				return acc;
			},
			{ day: "", likes: 0 }
		);

		document.querySelector('.total-likes .t-content p').textContent = `${formatNumbers(total_likes)} Likes`;
		document.querySelector('.total-comments .t-content p').textContent = `${formatNumbers(total_comments)} Comments`;
		document.querySelector('.total-shares .t-content p').textContent = `${formatNumbers(total_shares)} Shares`;

		document.querySelector('.top-month .t-content p').textContent = `${top_month_per_likes.month}`;
		document.querySelector('.top-day-of-week .t-content p').textContent = `${get_day_of_the_week_by_name(top_day_of_the_week_per_likes?.day || 0)}`;

		// top post per likes
		const top_post_per_likes = merged_formatted_data.reduce(
			(acc, curr) => {
				if (curr.likes > acc.likes) {
					return {
						post: curr,
						likes: curr.likes,
					};
				}
				return acc;
			},
			{ post: {}, likes: 0 }
		)
		const post_el = document.querySelector('.top-post-sample')
		post_el.querySelector('.w-img img').src = `https://robohash.org/${top_post_per_likes?.post?.likes}?set=set2`;
		// post_el.querySelector('.media-body h6').textContent = 
		post_el.querySelector('.meta-date-time').textContent = `${top_post_per_likes?.post?.date?.toLocaleString()}` 
		post_el.querySelector('.widget-content > p').textContent = `${top_post_per_likes?.post?.content}`
		post_el.querySelector('.w-action .card-like span').textContent = `${formatNumbers(top_post_per_likes?.likes)} Likes`

		let platform_url = ''
		
		if(top_post_per_likes?.post?.source === 'facebook') {
			platform_url = user_details_res['face_url']
		} else if(top_post_per_likes?.post?.source === 'instagram') {
			platform_url = user_details_res['insta']
		} else if(top_post_per_likes?.post?.source === 'twitter') {
			platform_url = user_details_res['twitter']
		}

		post_el.querySelector('.media-body h6').textContent = `@${getUsernameFromURL(platform_url) || '@JohnDoe'}`
		post_el.querySelector('.read-more a').href = platform_url



		// group stats by month
		const groupedDataByMonth = {};

		merged_formatted_data.forEach((post) => {
			if (!groupedDataByMonth[post.month]) {
				groupedDataByMonth[post.month] = {
					likes: 0,
					comments: 0,
					shares: 0,
				};
			}
			groupedDataByMonth[post.month].likes += post.likes;
			groupedDataByMonth[post.month].comments += post.comments;
			groupedDataByMonth[post.month].shares += post.shares;
		});

		
		const chart_months_sorted = Object.keys(groupedDataByMonth).sort((a,b) => {
			return month_names.indexOf(a) - month_names.indexOf(b);
		})

		var d_1options1 = {
			chart: {
				height: 350,
				type: "bar",
				toolbar: {
					show: false,
				},
				zoom: {
					enabled: true
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
			colors: ["#5c1ac3", "#ffbb44", "#ff8844"],
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
					name: "Likes",
					data: chart_months_sorted.map((month) => groupedDataByMonth[month].likes),
				},
				{
					name: "Comments",
					data: chart_months_sorted.map((month) => groupedDataByMonth[month].comments),
				},
				{
					name: "Shares",
					data: chart_months_sorted.map((month) => groupedDataByMonth[month].shares),
				},
			],
			xaxis: {
				categories: chart_months_sorted,
			},
			yaxis: {
				logarithmic: false,
				logBase: 10,
				tickAmount: 6,
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

		var d_1C_3 = new ApexCharts(
			document.querySelector("#uniqueVisits"),
			d_1options1
		);
		d_1C_3.render();


		// show dom elements
		social_media_monitoring_charts_wrapper.style.display = 'flex'
		charts_loader.style.display = 'none'
		
	})();

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


function formatNumbers(n) {
	return n.toString().replace(/\B(?=(\d{3})+(?!\d))/g, ",");
}

function getUsernameFromURL(url) {
	const parts = url.split("/")?.filter((part) => part.length > 0);
	return parts?.[parts.length - 1];
}