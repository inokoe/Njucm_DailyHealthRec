# Njucm_DailyHealthRec
适用于 NJUCM 的每日自动健康打卡

[![NjucmDailyRec](https://github.com/inokoe/Njucm_DailyHealthRec/actions/workflows/NjucmDailyRec.yml/badge.svg)](https://github.com/inokoe/Njucm_DailyHealthRec/actions/workflows/NjucmDailyRec.yml)
[![NjucmSessionCheck](https://github.com/inokoe/Njucm_DailyHealthRec/actions/workflows/NjucmSessionCheck.yml/badge.svg)](https://github.com/inokoe/Njucm_DailyHealthRec/actions/workflows/NjucmSessionCheck.yml)

# 思路
数据提交页面采用JSession,默认30分钟有效，过期则下发新JSession。
则保持于30分钟内至少有一次请求即可保持JSession始终有效，已达到自动化实现。
