# -*- encoding: utf-8 -*-
# @ModuleName: MeterSphere
# @Author: Moon-du
# @Personal website: ysbzc.com
# @CreateTime: 2021/6/11 22:47

import random, string

seeds = string.digits
ran_digit = random.sample(seeds, k=3)
app_suffix = "".join(ran_digit)

vars.put("applicationCaption", "application" + app_suffix)
vars.put("applicationName", "application" + app_suffix)
