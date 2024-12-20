import pandas as pd

calc_eng2chn = {
    "count": "数量",
    "max": "最大值",
    "min": "最小值",
    "mean": "平均值",
    "median": "中位数",
    "sum": "总和",
    "std": "标准差",
}

calc_templates = {
    "count": "count(cast({} as float)) as {}, -- {}",
    "max": "max(cast({} as float)) as {}, -- {}",
    "min": "min(cast({} as float)) as {}, -- {}",
    "mean": "avg(cast({} as float)) as {}, -- {}",
    "median": "percentile_approx(cast({} as float), 0.5) as {}, -- {}",
    "sum": "sum(cast({} as float)) as {}, -- {}",
    "std": "stddev_samp(cast({} as float)) as {}, -- {}",
}

credit_debt_summary_categories__eng2chn = {
    "ncl": "非循环贷账户",
    "cl1": "循环额度下分账户",
    "cl2": "循环贷账户",
    "cc": "贷记卡账户",
    "cc1": "准贷记卡账户",
    "mg": "相关还款责任",
}

dimensions_eng2chn = {
    "credit_default": "信贷交易违约信息概要",
}

feature_list = []

df_rst = pd.DataFrame()

def preprocess_tool(dic, colname, sql_code_template = None):
    feature_list.append(dic)
    if sql_code_template is None:
        return
    print(sql_code_template.format(colname, dic["feat_eng_name"], dic["feat_chn_name"]))


#################
## 信贷交易违约信息概要-->逾期（透支信息汇总）
#################
for cate in credit_debt_summary_categories__eng2chn:
    if cate == "mg":
        continue
    ## 原始
    feature_list.append({
        "feat_eng_name": f"pboc_{cate}_overdue_account_cnt",
        "feat_chn_name": f"“账户类型”为“{credit_debt_summary_categories__eng2chn[cate]}”的账户数",
    })
    feature_list.append({
        "feat_eng_name": f"pboc_{cate}_overdue_mth_cnt",
        "feat_chn_name": f"“账户类型”为“{credit_debt_summary_categories__eng2chn[cate]}”的月份数",
    })
    feature_list.append({
        "feat_eng_name": f"pboc_{cate}_overdue_max_amt",
        "feat_chn_name": f"“账户类型”为“{credit_debt_summary_categories__eng2chn[cate]}”的单月最高逾期总额",
    })
    feature_list.append({
        "feat_eng_name": f"pboc_{cate}_overdue_longest_mths",
        "feat_chn_name": f"“账户类型”为“{credit_debt_summary_categories__eng2chn[cate]}”的最长逾期/透支月数",
    })

feature_list.append({
    "feat_eng_name": "pboc_overdue_type_cnt",
    "feat_chn_name": "账户类型数",
})
feature_list.append({
    "feat_eng_name": "pboc_overdue_type_prop",
    "feat_chn_name": "账户类型占比",
})
## 聚合方向1
for calc in calc_eng2chn:
    # if calc == "count":
    #     continue
    preprocess_tool(
        {
            "feat_eng_name": f"pboc_overdue_account_cnt_{calc}",
            "feat_chn_name": f"各种“账户类型”下“账户数”的{calc_eng2chn[calc]}",
        },
        "accout_num",
        calc_templates[calc]
    )
    preprocess_tool(
        {
            "feat_eng_name": f"pboc_overdue_mth_cnt_{calc}",
            "feat_chn_name": f"各种“账户类型”下“月份数”的{calc_eng2chn[calc]}",
        },
        "month_num",
        calc_templates[calc]
    )
    preprocess_tool(
        {
            "feat_eng_name": f"pboc_overdue_max_amt_{calc}",
            "feat_chn_name": f"各种“账户类型”下“单月最高逾期/透支总额”的{calc_eng2chn[calc]}",
        },
        "maxoverdue_sum",
        calc_templates[calc]
    )
    preprocess_tool(
        {
            "feat_eng_name": f"pboc_overdue_longest_mths_{calc}",
            "feat_chn_name": f"各种“账户类型”下“最长逾期/透支月数”的{calc_eng2chn[calc]}",
        },
        "maxoverdue_mon",
        calc_templates[calc]
    )
    print()


## 聚合方向2
for item_eng, item_chn in zip(
    ["account_cnt", "mth_cnt", "max_amt", "longest_mths"],
    ["账户数", "月份数", "单月最高逾期总额", "最长逾期/透支月数"],
    # ["accout_num", "month_num", "maxoverdue_sum", "maxoverdue_mon"],
):

    range_feas = []
    for ct in [ct for ct in credit_debt_summary_categories__eng2chn.keys() if ct !="mg"]:
        range_feas.append(f"cast(pboc_{ct}_overdue_{item_eng} as float)")
    # print(range_feas)

    for cate in credit_debt_summary_categories__eng2chn:
        if cate == "mg":
            continue


        feature_list.append({
            "feat_eng_name": f"pboc_overdue_{item_eng}_max_cate_is_{cate}",
            "feat_chn_name": f"“{item_chn}”最大的“账户类型”是“{credit_debt_summary_categories__eng2chn[cate]}”与否",
        })
        cmd = f'''if(greatest({",".join(range_feas)})=cast(pboc_{cate}_overdue_{item_eng} as float), 1, 0) as pboc_overdue_{item_eng}_max_cate_is_{cate}, --“{item_chn}”最大的“账户类型”是“{credit_debt_summary_categories__eng2chn[cate]}”与否'''
        print(cmd)


        feature_list.append({
            "feat_eng_name": f"pboc_overdue_{item_eng}_min_cate_is_{cate}",
            "feat_chn_name": f"“{item_chn}”最小的“账户类型”是“{credit_debt_summary_categories__eng2chn[cate]}”与否",
        })
        cmd = f'''if(least({",".join(range_feas)})=cast(pboc_{cate}_overdue_{item_eng} as float), 1, 0) as pboc_overdue_{item_eng}_min_cate_is_{cate}, --“{item_chn}”最小的“账户类型”是“{credit_debt_summary_categories__eng2chn[cate]}”与否'''
        print(cmd)

        print()





df_here = pd.DataFrame(feature_list)
df_here["dim1"] = "信息概要"
df_here["dim2"] = "信贷交易违约信息概要"
df_here["dim3"] = "逾期(透支)信息汇总"
df_rst = pd.concat([df_rst, df_here]).reset_index(drop=True)



##########
df_here[["dim1", "dim2", "dim3", "feat_eng_name", "feat_chn_name"]].to_csv("信贷交易违约信息概要.csv", index=False)



