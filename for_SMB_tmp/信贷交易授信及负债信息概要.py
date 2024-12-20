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

credit_debt_summary_categories__eng2chn = {
    "ncl": "非循环贷账户",
    "cl1": "循环额度下分账户",
    "cl2": "循环贷账户",
    "cc": "贷记卡账户",
    # "cc1": "准贷记卡账户",
    "mg": "相关还款责任",
}

feature_list = []

df_rst = pd.DataFrame()

feature_list.append({
    "feat_eng_name": "pboc_type_cnt",
    "feat_chn_name": "“信贷交易授信及负债信息概要”下，账户类型数",
})
feature_list.append({
    "feat_eng_name": "pboc_type_prop",
    "feat_chn_name": "“信贷交易授信及负债信息概要”下，账户类型占比",
})

## （各种的，分开考虑）
for cate in credit_debt_summary_categories__eng2chn:
    # feature_list.append({
    #     "dim3": f"{credit_debt_summary_categories__eng2chn[cate]}信息汇总",
    #     "feat_eng_name": f"pboc_{cate}_exists",
    #     "feat_chn_name": f"“信贷交易授信及负债信息概要”下，“{credit_debt_summary_categories__eng2chn[cate]}信息汇总”栏目是否存在",
    # })
    if cate in ["ncl", "cl1", "cl2"]:
        ## 原始字段：
        for item_eng, item_chn in zip(
            ["org_cnt", "account_cnt", "credit_amt", "balance_amt", "needpay_6m_avg_amt"],
            ["管理机构数", "账户数", "授信总额", "余额", "最近6个月平均应还款"]
        ):
            feature_list.append({
                "dim3": f"{credit_debt_summary_categories__eng2chn[cate]}信息汇总",
                "feat_eng_name": f"pboc_{cate}_{item_eng}",
                "feat_chn_name": f"“信贷交易授信及负债信息概要”下，“{credit_debt_summary_categories__eng2chn[cate]}信息汇总”的“{item_chn}”",
            })
        ## 衍生
        feature_list.append({
            "dim3": f"{credit_debt_summary_categories__eng2chn[cate]}信息汇总",
            "feat_eng_name": f"pboc_{cate}_balance_amt_div_credit_amt",
            "feat_chn_name": f"“信贷交易授信及负债信息概要”下，“{credit_debt_summary_categories__eng2chn[cate]}信息汇总”中余额与授信总额的比值",
        })
        for item_eng, item_chn in zip(
                ["account_cnt", "credit_amt", "balance_amt", "shouldpay_6m_avg_amt"],
                ["账户数", "授信总额", "余额", "最近6个月平均应还款"]
        ):
            feature_list.append({
                "dim3": f"{credit_debt_summary_categories__eng2chn[cate]}信息汇总",
                "feat_eng_name": f"pboc_{cate}_{item_eng}_avg",
                "feat_chn_name": f"“信贷交易授信及负债信息概要”下，“{credit_debt_summary_categories__eng2chn[cate]}信息汇总”的每个管理机构下“{item_chn}”的平均值",
            })
        for item_eng, item_chn in zip(
                ["credit_amt", "balance_amt", "shouldpay_6m_avg_amt"],
                ["授信总额", "余额", "最近6个月平均应还款"]
        ):
            feature_list.append({
                "dim3": f"{credit_debt_summary_categories__eng2chn[cate]}信息汇总",
                "feat_eng_name": f"pboc_{cate}_{item_eng}_avg",
                "feat_chn_name": f"“信贷交易授信及负债信息概要”下，“{credit_debt_summary_categories__eng2chn[cate]}信息汇总”的每个账户下“{item_chn}”的平均值",
            })
    elif cate in ["cc",]:
        ## 原始字段：
        for item_eng, item_chn in zip(
                ["org_cnt", "account_cnt", "credit_sum_amt", "credit_max_amt",  "credit_min_amt", "balance_amt", "needpay_6m_avg_amt"],
                ["发卡机构数", "账户数", "授信总额", "单家行最高授信额", "单家行最低授信额", "已用额度", "最近6个月平均使用额度"]
        ):
            feature_list.append({
                "dim3": f"{credit_debt_summary_categories__eng2chn[cate]}信息汇总",
                "feat_eng_name": f"pboc_{cate}_{item_eng}",
                "feat_chn_name": f"“信贷交易授信及负债信息概要”下，“{credit_debt_summary_categories__eng2chn[cate]}信息汇总”的“{item_chn}”",
            })
        ## 衍生：
        feature_list.append({
            "dim3": f"{credit_debt_summary_categories__eng2chn[cate]}信息汇总",
            "feat_eng_name": f"pboc_{cate}_credit_max_amt_minus_min_amt",
            "feat_chn_name": f"“信贷交易授信及负债信息概要”下，“{credit_debt_summary_categories__eng2chn[cate]}信息汇总”的单家最高最低授信额差值",
        })
        feature_list.append({
            "dim3": f"{credit_debt_summary_categories__eng2chn[cate]}信息汇总",
            "feat_eng_name": f"pboc_{cate}_credit_max_amt_div_min_amt",
            "feat_chn_name": f"“信贷交易授信及负债信息概要”下，“{credit_debt_summary_categories__eng2chn[cate]}信息汇总”的单家最高最低授信额比值",
        })
        feature_list.append({
            "dim3": f"{credit_debt_summary_categories__eng2chn[cate]}信息汇总",
            "feat_eng_name": f"pboc_{cate}_balance_amt_div_credit_sum_amt",
            "feat_chn_name": f"“信贷交易授信及负债信息概要”下，“{credit_debt_summary_categories__eng2chn[cate]}信息汇总”的已用额度和总额度的比值",
        })
        feature_list.append({
            "dim3": f"{credit_debt_summary_categories__eng2chn[cate]}信息汇总",
            "feat_eng_name": f"pboc_{cate}_needpay_6m_avg_amt_div_balance_amt",
            "feat_chn_name": f"“信贷交易授信及负债信息概要”下，“{credit_debt_summary_categories__eng2chn[cate]}信息汇总”的“最近6个月平均使用额度”和“已用额度”的比值",
        })
        feature_list.append({
            "dim3": f"{credit_debt_summary_categories__eng2chn[cate]}信息汇总",
            "feat_eng_name": f"pboc_{cate}_needpay_6m_avg_amt_div_credit_sum_amt",
            "feat_chn_name": f"“信贷交易授信及负债信息概要”下，“{credit_debt_summary_categories__eng2chn[cate]}信息汇总”的“最近6个月平均使用额度”和“授信总额”的比值",
        })
        for item_eng, item_chn in zip(
                ["account_cnt", "credit_sum_amt", "balance_amt", "needpay_6m_avg_amt"],
                ["账户数", "授信总额", "已用额度", "最近6个月平均使用额度"]
        ):
            feature_list.append({
                "dim3": f"{credit_debt_summary_categories__eng2chn[cate]}信息汇总",
                "feat_eng_name": f"pboc_{cate}_{item_eng}_every_org",
                "feat_chn_name": f"“信贷交易授信及负债信息概要”下，“{credit_debt_summary_categories__eng2chn[cate]}信息汇总”，平均每个机构下“{item_chn}”的值",
            })
    elif cate in ["mg"]:
        for for_who in zip(
            ["for_person", "for_ent", ],
            ["为个人", "为企业", ]
        ):
            for tpe in zip(
                ["grt_resp", "other_resp", ],
                ["担保责任", "其他相关还款责任", ]
            ):
                for itm in zip(
                    ["account_cnt", "grt_amt", "resp_amt", "balance_amt",],
                    ["账户数", "担保金额", "还款责任金额", "余额",]
                ):
                    if (tpe[0] == "grt_resp") and (itm[0] == "resp_amt"):
                        continue
                    if (tpe[0] == "other_resp") and (itm[0] == "grt_amt"):
                        continue
                    feature_list.append({
                        "dim3": f"{credit_debt_summary_categories__eng2chn[cate]}信息汇总",
                        "feat_eng_name": f"pboc_{cate}_{for_who[0]}_{tpe[0]}_{itm[0]}",
                        "feat_chn_name": f"“信贷交易授信及负债信息概要”下，“{credit_debt_summary_categories__eng2chn[cate]}信息汇总”的“{for_who[1]}·{tpe[1]}·{itm[1]}”",
                    })
                # if tpe[0] == "grt_resp":
            feature_list.append({
                "dim3": f"{credit_debt_summary_categories__eng2chn[cate]}信息汇总",
                "feat_eng_name": f"pboc_{cate}_{for_who[0]}_grt_resp_balance_amt_div_grt_amt",
                "feat_chn_name": f"“信贷交易授信及负债信息概要”下，“{credit_debt_summary_categories__eng2chn[cate]}信息汇总”的“为个人·担保责任”中余额和担保金额的比值",
            })
            feature_list.append({
                "dim3": f"{credit_debt_summary_categories__eng2chn[cate]}信息汇总",
                "feat_eng_name": f"pboc_{cate}_{for_who[0]}_other_resp_balance_amt_div_resp_amt",
                "feat_chn_name": f"“信贷交易授信及负债信息概要”下，“{credit_debt_summary_categories__eng2chn[cate]}信息汇总”的“为个人·其他相关还款责任”中余额和还款责任金额的比值",
            })
    else:
        pass

## （【种】里面除了相关还款责任的种类，合在一起统计）
for itm in zip(
    ["credit_amt", "balance_amt", "needpay_6m_avg_amt"],
    ["账户数", "授信总额", "余额", "最近6个月平均应还款"]
):
    for calc in calc_eng2chn:
        if calc == "count":
            continue
        feature_list.append({
            "dim3": f"{credit_debt_summary_categories__eng2chn[cate]}信息汇总",
            "feat_eng_name": f"pboc_credit_debt_summary_{itm[0]}_{calc}",
            "feat_chn_name": f"“信贷交易授信及负债信息概要”下，“{itm[1]}”的{calc_eng2chn[calc]}",
        })
    for cate in credit_debt_summary_categories__eng2chn:
        if cate == "mg":
            continue
        feature_list.append({
            "dim3": f"{credit_debt_summary_categories__eng2chn[cate]}信息汇总",
            "feat_eng_name": f"pboc_credit_debt_summary_{itm[0]}_max_cat_is_{cate}",
            "feat_chn_name": f"“信贷交易授信及负债信息概要”下，“{itm[1]}”值最大的种类是{credit_debt_summary_categories__eng2chn[cate]}",
        })
        feature_list.append({
            "dim3": f"{credit_debt_summary_categories__eng2chn[cate]}信息汇总",
            "feat_eng_name": f"pboc_credit_debt_summary_{itm[0]}_min_cat_is_{cate}",
            "feat_chn_name": f"“信贷交易授信及负债信息概要”下，“{itm[1]}”值最小的种类是{credit_debt_summary_categories__eng2chn[cate]}",
        })




# #################
# ## 信贷交易违约信息概要-->逾期（透支信息汇总）
# #################
# for cate in credit_debt_summary_categories__eng2chn:
#     if cate == "mg":
#         continue
#     ## 原始
#     feature_list.append({
#         "feat_eng_name": f"pboc_{cate}_overdue_account_cnt",
#         "feat_chn_name": f"“账户类型”为“{credit_debt_summary_categories__eng2chn[cate]}”的账户数",
#     })
#     feature_list.append({
#         "feat_eng_name": f"pboc_{cate}_overdue_mth_cnt",
#         "feat_chn_name": f"“账户类型”为“{credit_debt_summary_categories__eng2chn[cate]}”的月份数",
#     })
#     feature_list.append({
#         "feat_eng_name": f"pboc_{cate}_overdue_max_amt",
#         "feat_chn_name": f"“账户类型”为“{credit_debt_summary_categories__eng2chn[cate]}”的单月最高逾期总额",
#     })
#     feature_list.append({
#         "feat_eng_name": f"pboc_{cate}_overdue_longest_mths",
#         "feat_chn_name": f"“账户类型”为“{credit_debt_summary_categories__eng2chn[cate]}”的最长逾期/透支月数",
#     })
#
# feature_list.append({
#     "feat_eng_name": "prob_overdue_type_cnt",
#     "feat_chn_name": "账户类型数",
# })
# feature_list.append({
#     "feat_eng_name": "prob_overdue_type_prop",
#     "feat_chn_name": "账户类型占比",
# })
# ## 聚合方向1
# for calc in calc_eng2chn:
#     if calc == "count":
#         continue
#     feature_list.append({
#         "feat_eng_name": f"pboc_overdue_account_cnt_{calc}",
#         "feat_chn_name": f"各种“账户类型”下“账户数”的{calc_eng2chn[calc]}",
#     })
#     feature_list.append({
#         "feat_eng_name": f"pboc_overdue_mth_cnt_{calc}",
#         "feat_chn_name": f"各种“账户类型”下“月份数”的{calc_eng2chn[calc]}",
#     })
#     feature_list.append({
#         "feat_eng_name": f"pboc_overdue_max_amt_{calc}",
#         "feat_chn_name": f"各种“账户类型”下“单月最高逾期总额”的{calc_eng2chn[calc]}",
#     })
#     feature_list.append({
#         "feat_eng_name": f"pboc_overdue_longest_mths_{calc}",
#         "feat_chn_name": f"各种“账户类型”下“最长逾期/透支月数”的{calc_eng2chn[calc]}",
#     })
#
# ## 聚合方向2
# for item_eng, item_chn in zip(
#     ["account_cnt", "mth_cnt", "max_amt", "longest_mths"],
#     ["账户数", "月份数", "单月最高逾期总额", "最长逾期/透支月数"]
# ):
#     for cate in credit_debt_summary_categories__eng2chn:
#         feature_list.append({
#             "feat_eng_name": f"pboc_overdue_{item_eng}_max_cate_is_{cate}",
#             "feat_chn_name": f"“{item_chn}”最大的“账户类型”是“{credit_debt_summary_categories__eng2chn[cate]}”与否",
#         })
#         feature_list.append({
#             "feat_eng_name": f"pboc_overdue_{item_eng}_min_cate_is_{cate}",
#             "feat_chn_name": f"“{item_chn}”最小的“账户类型”是“{credit_debt_summary_categories__eng2chn[cate]}”与否",
#         })

df_here = pd.DataFrame(feature_list)
df_here["dim1"] = "信息概要"
df_here["dim2"] = "信贷交易授信与负债信息概要"
# df_here["dim3"] = "逾期(透支)信息汇总"
df_rst = pd.concat([df_rst, df_here]).reset_index(drop=True)



##########
df_here[["dim1", "dim2", "dim3", "feat_eng_name", "feat_chn_name"]].to_csv("信贷交易授信及负债信息概要.csv", index=False)



