import json
import secrets
from django.db.models import Q
from django.http import JsonResponse
from django.shortcuts import render,HttpResponse,redirect
from openai import OpenAI
import pandas as pd
import numpy as np
from datetime import datetime
from huaqi import models
from reportlab.lib.pagesizes import A4
from reportlab.lib.units import inch
from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
import re
# Create your views here.
def login(request):
    global global_user_type
    if request.method == "POST":
        data = json.loads(request.body)
        username = data.get('username')
        password =data.get('password')
        print(username,password)

        access_token=secrets.token_hex(32)
        obj_user=models.userInfo.objects.filter(name=username,password=password).first()
        # obj_user = ["k"]
        if obj_user is not None :
        #   print(obj_user.account_name)
        #   request.session['user_type'] = obj_user.user_type
          global_user_type={'user_type':obj_user.user_type}
          return JsonResponse({
             'success': True,
             'message': '登录成功',
             'data_user': {
                 'user': {
                     'name': obj_user.name,
                     'user_password':obj_user.password,
                     'type': obj_user.user_type,
                     'account_name': obj_user.account_name,
                     'email': obj_user.email,
                     'accessToken': access_token,
                 }
             }
          })
        else:
           print("shibai")
           # 用户验证失败
           return JsonResponse({
             'success': False,
             'message': '用户名或密码错误',
             'data_user': {
                 'user': {
                     'name': None,
                     'user_password':None,
                     'type': None,
                     'account_name': None,
                     'email': None,
                     'accessToken': None,
                 }
             }
         })

def register(request):
    if request.method == "POST":
        global global_user_type
        data = json.loads(request.body)
        username = data.get('username')
        password =data.get('password')
        confirm_password =data.get('ConfirmPassword')
        user_type =data.get('category')
        email =data.get('email')
        print(username,password,confirm_password,email)
        global_user_type = {
            'user_type': user_type,
        }
        if password != confirm_password:
            return JsonResponse({'status': 'error', 'message': '两次密码不一致，请重新设置密码'})
        elif models.userInfo.objects.filter(name=username).exists():
            return JsonResponse({'status': 'error', 'message': '账号已存在，请换一个'})
        else:
         models.userInfo.objects.create(name=username,password=password,user_type=user_type,email=email)
         return JsonResponse({'status': 'ok', 'message': '注册成功'})





def submit_view(request):
    #if request.method == "GET":
        #return render(request, 'submit.html')
    if request.method == 'POST':
        try:
            # 获取前端发送的 JSON 数据
            data = json.loads(request.body)
            country = data.get('country')
            dates = data.get('date')
            countries=data.get('countries',[])
            print(country,dates,countries)
            eurozone_countries = [
                "Austria", "Belgium", "Croatia", "Cyprus", "Estonia", "Finland", "France",
                "Germany", "Greece", "Ireland", "Italy", "Latvia", "Lithuania", "Luxembourg",
                "Malta", "Netherlands", "Portugal", "Slovakia", "Slovenia", "Spain"
            ]
            if country=='United States':
                obj_us=models.earth_rate.objects.filter(country='United_States').first()
                return JsonResponse({'message': 'Hello from Django!',
                                     'table_data': {
                                         'currency': obj_us.currency,
                                         'currency_sign': obj_us.currency_sign,
                                         'currency1_name': obj_us.currency1_name,
                                         'currency_rate1': obj_us.currency_rate1,
                                         'currency2_name': obj_us.currency2_name,
                                         'currency_rate2': obj_us.currency_rate2,
                                         'currency3_name': obj_us.currency3_name,
                                         'currency_rate3': obj_us.currency_rate3,
                                         'currency4_name': obj_us.currency4_name,
                                         'currency_rate4': obj_us.currency_rate4,
                                         'currency5_name': obj_us.currency5_name,
                                         'currency_rate5': obj_us.currency_rate5,
                                         'currency6_name': obj_us.currency6_name,
                                         'currency_rate6': obj_us.currency_rate6,
                                         'currency7_name': obj_us.currency7_name,
                                         'currency_rate7': obj_us.currency_rate7,
                                         'currency8_name': obj_us.currency8_name,
                                         'currency_rate8': obj_us.currency_rate8,
                                         'currency9_name': obj_us.currency9_name,
                                         'currency_rate9': obj_us.currency_rate9
                                     }})
            if country in eurozone_countries:
                obj_euro = models.earth_rate.objects.filter(country='EURO').first()
                print(obj_euro.currency,obj_euro.currency_sign,obj_euro.currency_rate1)
              #
              #
                return JsonResponse({'message': 'Hello from Django!',
                   'table_data': {
                       'currency':obj_euro.currency,
                       'currency_sign':obj_euro.currency_sign,
                       'currency1_name':obj_euro.currency1_name,
                       'currency_rate1':obj_euro.currency_rate1,
                       'currency2_name':obj_euro.currency2_name,
                       'currency_rate2':obj_euro.currency_rate2,
                       'currency3_name':obj_euro.currency3_name,
                       'currency_rate3':obj_euro.currency_rate3,
                       'currency4_name':obj_euro.currency4_name,
                       'currency_rate4':obj_euro.currency_rate4,
                       'currency5_name':obj_euro.currency5_name,
                       'currency_rate5':obj_euro.currency_rate5,
                       'currency6_name':obj_euro.currency6_name,
                       'currency_rate6':obj_euro.currency_rate6,
                       'currency7_name':obj_euro.currency7_name,
                       'currency_rate7':obj_euro.currency_rate7,
                       'currency8_name':obj_euro.currency8_name,
                       'currency_rate8':obj_euro.currency_rate8,
                       'currency9_name':obj_euro.currency9_name,
                       'currency_rate9':obj_euro.currency_rate9
                   }})
            if (country and dates) is not  None :
              obj = models.earth_rate.objects.filter(country=country, date_time=dates).first()
              print(obj.currency,obj.currency_sign,obj.currency_rate1)
              return JsonResponse({'message': 'Hello from Django!',
                   'table_data': {
                       'currency':obj.currency,
                       'currency_sign':obj.currency_sign,
                       'currency1_name':obj.currency1_name,
                       'currency_rate1':obj.currency_rate1,
                       'currency2_name':obj.currency2_name,
                       'currency_rate2':obj.currency_rate2,
                       'currency3_name':obj.currency3_name,
                       'currency_rate3':obj.currency_rate3,
                       'currency4_name':obj.currency4_name,
                       'currency_rate4':obj.currency_rate4,
                       'currency5_name':obj.currency5_name,
                       'currency_rate5':obj.currency_rate5,
                       'currency6_name':obj.currency6_name,
                       'currency_rate6':obj.currency_rate6,
                       'currency7_name':obj.currency7_name,
                       'currency_rate7':obj.currency_rate7,
                       'currency8_name':obj.currency8_name,
                       'currency_rate8':obj.currency_rate8,
                       'currency9_name':obj.currency9_name,
                       'currency_rate9':obj.currency_rate9
                   }})

        except json.JSONDecodeError:
            return JsonResponse({'status': 'error', 'message': '无效的 JSON 数据'}, status=400)
        except Exception as e:
            return JsonResponse({'status': 'error', 'message': str(e)}, status=500)
# 波动率评级函数
# 波动率评级函数
def rate_volatility(std_dev, percentiles):
  if std_dev < percentiles[0.25]:
    return '低波动性'
  elif std_dev < percentiles[0.5]:
    return '较低波动性'
  elif std_dev < percentiles[0.75]:
    return '中等波动性'
  elif std_dev < percentiles[0.90]:
    return '较高波动性'
  else:
    return '高波动性'

def max_drawdown(df):
    """计算最大回撤"""
    if df.empty:
        print("!!!该时间段无数据")
        return 0
    # 定义原始列表
    original_list = list(df['predict_rate'])
    # 存储新列表
    new_list = []
    # 存储列表第一个值
    current_value = original_list[0]
    # 遍历原始列表
    for value in original_list:
        if value > current_value:
            new_list.append(value)
            current_value = value
        else:
            new_list.append(current_value)
    new_list = np.array(new_list)
    original_list = np.array(original_list)
    res_list = list((new_list-original_list)/original_list*100)
    # 定义原始列表
    original_list2 = list(df['true_rate'])
    # 存储新列表
    new_list2 = []
    # 存储列表第一个值
    current_value2 = original_list2[0]
    # 遍历原始列表
    for value in original_list2:
        if value > current_value2:
            new_list2.append(value)
            current_value2 = value
        else:
            new_list2.append(current_value2)
    new_list2 = np.array(new_list2)
    original_list2 = np.array(original_list2)
    res_list2 = list((new_list2-original_list2)/original_list2*100)
    return res_list,res_list2


def currency_pair(request):
    print(request.body)
    if request.method == 'POST':
        try:
            # 获取前端发送的 JSON 数据
            data = json.loads(request.body)
            countries = data.get('countries')
            print(countries)
            country_1 = countries[0]
            print(country_1)
            country_2 = countries[1]
            print(country_2)
            deal_year = data.get('investmentPeriod')
            if deal_year == 1:
                deal_year = '1年'
            elif deal_year == 3:
                deal_year = '3年'
            elif deal_year == 5:
                deal_year = '5年'
            print(deal_year)
            date_start = datetime.strptime(data.get('startDate'), "%Y-%m-%d")
            date_start = date_start.strftime("%Y-%m-%d")
            print(date_start)
            date_end = datetime.strptime(data.get('endDate'), "%Y-%m-%d")
            date_end = date_end.strftime("%Y-%m-%d")
            print(date_end)
            maxDrawdown = data.get('maxDrawdown')
            eurozone_countries = [
                "Austria", "Belgium", "Croatia", "Cyprus", "Estonia", "Finland", "France",
                "Germany", "Greece", "Ireland", "Italy", "Latvia", "Lithuania", "Luxembourg",
                "Malta", "Netherlands", "Portugal", "Slovakia", "Slovenia", "Spain"
            ]
            if country_1  in eurozone_countries and country_2 in eurozone_countries:
                return JsonResponse({'status': 'error', 'message': '两个欧元国家'})
            else:
                if country_1 == 'United States' :
                     country_1 = 'United_States'
                if country_2 == 'United States' :
                     country_2 = 'United_States'
                print('here1')
                currency_1 = models.country_currency.objects.filter(country=country_1).first().currency
                print(currency_1)
                currency_2 = models.country_currency.objects.filter(country=country_2).first().currency
                print(currency_2)
                obj = models.date_currency_rates.objects.filter(
                    currency_1=currency_1,
                    currency_2=currency_2,
                    date_time__gte=date_start,  # 大于等于 start datetime
                    date_time__lte=date_end,     # 小于等于 end datetime
                    deal_year=deal_year
                )
                date_time_list = list(obj.values_list('date_time', flat=True))
                predict_rate_list = list(obj.values_list('predict_rate', flat=True))
                true_rate_list = list(obj.values_list('true_rate', flat=True))
                da = {
                    'date_time': pd.to_datetime(date_time_list),
                    'predict_rate': np.array(predict_rate_list, dtype=float),
                    'true_rate': np.array(true_rate_list, dtype=float),
                }
                df = pd.DataFrame(da)
                std_dev = df['predict_rate'].std()
                print(std_dev)
                percentiles = {0.25:0.0008, 0.50:0.0101, 0.75:0.1020, 0.90:1.5048}
                volatility_rate = rate_volatility(std_dev, percentiles)
                print(volatility_rate)
                maxdd_p,maxdd_t = max_drawdown(df)
                print('maxdd')
                # identity_user=request.session.get('user_type')
                identity_user=global_user_type.get('user_type')
                print(identity_user)
                temp = False
                for value in maxdd_p:
                    if value >= maxDrawdown:
                        temp = True
                        break
                print(maxDrawdown)
                temp2 = False
                for value in maxdd_t:
                    if value >= maxDrawdown:
                        temp2 = True
                        break
                if temp or temp2:
                    ai_result =  deepseek_generate(date_start,date_end,[currency_1,currency_2],[country_1,country_2],[maxdd_p,maxdd_t],maxDrawdown,identity_user,std_dev)
                else:
                    ai_result = '无风险'
                return JsonResponse({'message': '获取成功',
                                     'data':{
                                         'date_time':date_time_list,
                                         'predict_rate':predict_rate_list,
                                         'true_rate':true_rate_list,
                                         'volatility_rate':volatility_rate,
                                         'maxdd_predict':maxdd_p,
                                         'maxdd_true':maxdd_t,
                                         'ai_result':ai_result
                                         }
                                    },status=201)
        except Exception as e:
            return JsonResponse({'status': 'error', 'message': str(e)}, status=501)


def multi_currency(request):
     if request.method == 'POST':
        try:
            # 解析请求体中的 JSON 数据
            data = json.loads(request.body)
            max_drawdown = data.get("maxDrawdown")
            dates = data.get('month')
            investment_period=data.get('investmentPeriod')
            print(max_drawdown,dates,investment_period)
            # dates='2024-08-01'
            # max_drawdown=-0.5
            # print(dates,max_drawdown)
            # 查询数据库中指定日期的记录
            if investment_period==5:
             queryset_pre_5 = models.ProcessedPreDrawdown.objects.filter(Date=dates)
             queryset_tar_5=models.ProcessedTarDrawdown.objects.filter(Date=dates)
             result1=find_multi_currency(queryset_pre_5,max_drawdown)
             result2=find_multi_currency(queryset_tar_5,max_drawdown)
             return JsonResponse({'result1':result1,'result2':result2})
            if investment_period==3:
                queryset_pre_3 = models.ProcessedPreDrawdown_3.objects.filter(Date=dates)
                queryset_tar_3=models.ProcessedTarDrawdown_3.objects.filter(Date=dates)
                result1=find_multi_currency(queryset_pre_3,max_drawdown)
                result2=find_multi_currency(queryset_tar_3,max_drawdown)
                return JsonResponse({'result1':result1,'result2':result2})
            if investment_period==1:
                queryset_pre_1 = models.ProcessedPreDrawdown_1.objects.filter(Date=dates)
                queryset_tar_1 = models.ProcessedTarDrawdown_1.objects.filter(Date=dates)
                result1=find_multi_currency(queryset_pre_1,max_drawdown)
                result2=find_multi_currency(queryset_tar_1,max_drawdown)
                return JsonResponse({'result1': result1, 'result2': result2})
        except Exception as e:
            return JsonResponse({"error": str(e)}, status=400)
     else:
        return JsonResponse({"error": "Invalid request method"}, status=405)
def find_multi_currency(queryset,max_drawdown):
    if queryset is not None:
        columns = [field.name for field in models.ProcessedPreDrawdown._meta.fields]
        print(columns)
        # 初始化结果对象
        result = {
            "nodes": [
                {
                    "color": "#F44336",
                    "label": "USD（美元）",
                    "attributes": {},
                    "y": -434.4221,
                    "x": -75.53079,
                    "id": "usd",
                    "size": 100.0
                },
                {
                    "color": "#E91E63",
                    "label": "EUR（欧元）",
                    "attributes": {},
                    "y": 41.25936,
                    "x": 157.57562,
                    "id": "eur",
                    "size": 73.161194
                },
                {
                    "color": "#03A9F4",
                    "label": "JPY（日元）",
                    "attributes": {},
                    "y": 241.89249,
                    "x": -147.57906,
                    "id": "jpy",
                    "size": 64.54965
                },
                {
                    "color": "#EF5350",
                    "label": "GBP（英镑）",
                    "attributes": {},
                    "y": -230.14833,
                    "x": -644.2716,
                    "id": "gbp",
                    "size": 49.608772
                },
                {
                    "color": "#EC407A",
                    "label": "CNY（人民币）",
                    "attributes": {},
                    "y": 171.80579,
                    "x": 599.53815,
                    "id": "cny",
                    "size": 48.6046
                },
                {
                    "color": "#29B6F6",
                    "label": "AUD（澳元）",
                    "attributes": {},
                    "y": -182.1726,
                    "x": -479.44443,
                    "id": "aud",
                    "size": 43.21858
                },
                {
                    "color": "#E57373",
                    "label": "CAD（加元）",
                    "attributes": {},
                    "y": -265.6326,
                    "x": 694.03375,
                    "id": "cad",
                    "size": 33.359425
                },
                {
                    "color": "#F06292",
                    "label": "CHF（瑞士法郎）",
                    "attributes": {},
                    "y": -224.0287,
                    "x": 317.77667,
                    "id": "chf",
                    "size": 23.713282
                },
                {
                    "color": "#EF9A9A",
                    "label": "SGD（新加坡元）",
                    "attributes": {},
                    "y": 120.37976,
                    "x": -710.59204,
                    "id": "sgd",
                    "size": 19.818306
                },
                {
                    "color": "#F48FB1",
                    "label": "KRW（韩元）",
                    "attributes": {},
                    "y": 294.88266,
                    "x": -933.4234,
                    "id": "krw",
                    "size": 19.574871
                },
                {
                    "color": "#4DD0E1",
                    "label": "INR（印度卢比）",
                    "attributes": {},
                    "y": -380.16626,
                    "x": 118.30771,
                    "id": "inr",
                    "size": 18.935852
                },
                {
                    "color": "#EF9A9A",
                    "label": "BRL（巴西雷亚尔）",
                    "attributes": {},
                    "y": 56.938953,
                    "x": -895.56586,
                    "id": "brl",
                    "size": 17.475237
                },
                {
                    "color": "#F48FB1",
                    "label": "MXN（墨西哥比索）",
                    "attributes": {},
                    "y": -75.5553,
                    "x": -880.5015,
                    "id": "mxn",
                    "size": 15.923333
                },
                {
                    "color": "#81D4FA",
                    "label": "SEK（瑞典克朗）",
                    "attributes": {},
                    "y": -542.05096,
                    "x": 502.02698,
                    "id": "sek",
                    "size": 14.88873
                },
                {
                    "color": "#FFCDD2",
                    "label": "NOK（挪威克朗）",
                    "attributes": {},
                    "y": 34.348167,
                    "x": -284.14108,
                    "id": "nok",
                    "size": 14.858301
                },
                {
                    "color": "#F8BBD0",
                    "label": "PLN（波兰兹罗提）",
                    "attributes": {},
                    "y": -389.02567,
                    "x": -423.78125,
                    "id": "pln",
                    "size": 12.54566
                },
                {
                    "color": "#B3E5FC",
                    "label": "TRY（土耳其里拉）",
                    "attributes": {},
                    "y": -792.2076,
                    "x": -998.14185,
                    "id": "try",
                    "size": 12.180507
                },
                {
                    "color": "#E8EAF6",
                    "label": "AED（阿联酋迪拉姆）",
                    "attributes": {},
                    "y": 695.1258,
                    "x": 881.2038,
                    "id": "aed",
                    "size": 11.845781
                },
                {
                    "color": "#FFEBEE",
                    "label": "SAR（沙特里亚尔）",
                    "attributes": {},
                    "y": 264.84995,
                    "x": -421.52237,
                    "id": "sar",
                    "size": 11.298051
                },
                {
                    "color": "#FFEBEE",
                    "label": "THB（泰铢）",
                    "attributes": {},
                    "y": 522.375,
                    "x": -1089.2416,
                    "id": "thb",
                    "size": 11.237192
                },
                {
                    "color": "#FFEBEE",
                    "label": "IDR（印尼盾）",
                    "attributes": {},
                    "y": 378.15536,
                    "x": -1150.2018,
                    "id": "idr",
                    "size": 10.81118
                },
                {
                    "color": "#FCE4EC",
                    "label": "ARS（阿根廷比索）",
                    "attributes": {},
                    "y": 649.42224,
                    "x": 320.47504,
                    "id": "ars",
                    "size": 10.14173
                },
                {
                    "color": "#E1F5FE",
                    "label": "RUB（俄罗斯卢布）",
                    "attributes": {},
                    "y": -620.4443,
                    "x": -586.76886,
                    "id": "rub",
                    "size": 10.020013
                }
            ],
            "edges": []
        }

        # 遍历查询结果
        for obj in queryset:
            # 遍历所有列名，找到形如 A_B 的列
            for col in columns:
                if '_' in col and col.split('_')[0] != col.split('_')[1]:
                    # 提取货币对
                    currency_pair = col.split('_')
                    currency_a = currency_pair[0]
                    currency_b = currency_pair[1]

                    # 获取当前列的值
                    drawdown_value = getattr(obj, col)

                    # 计算比例
                    if max_drawdown != 0:
                        ratio = drawdown_value / max_drawdown
                    else:
                        ratio = 0

                    # 将比例填入对应货币对的 edge 部分
                    # 查找是否已经存在该货币对的 edge（无论是 A_B 还是 B_A）
                    existing_edge_ab = next((edge for edge in result['edges'] if
                                             edge['sourceID'] == currency_a and edge['targetID'] == currency_b),
                                            None)
                    existing_edge_ba = next((edge for edge in result['edges'] if
                                             edge['sourceID'] == currency_b and edge['targetID'] == currency_a),
                                            None)

                    if existing_edge_ab:
                        existing_edge_ab['size'] = ratio
                    elif existing_edge_ba:
                        existing_edge_ba['size'] = ratio
                    else:
                        # 如果不存在，则添加新的 edge
                        result['edges'].append({
                            "sourceID": currency_a,
                            "targetID": currency_b,
                            "attributes": {},
                            "size": ratio
                        })
        print(result)
    return result
def deepseek_generate(dates_begin,dates_end,currency_pair,countries,drawdown,maxdrawdown,identify,flex_rate):

        # 从数据库中获取数据
        data_dict = get_data_from_db(dates_begin,dates_end,currency_pair,countries,drawdown)

        # 根据数据库中的数据组织一次提问
        query = generate_query(currency_pair, data_dict,maxdrawdown,identify,flex_rate)

        # 使用大模型进行回答
        response_ai = chat_completions(query)
        return response_ai

def get_data_from_db(dates_begin, dates_end, currency_pair,countries,drwadown):
    data_dict = {}
    print(data_dict)
    try:
        data_dict['dates_begin']=dates_begin
        data_dict['dates_end']=dates_end
        data_dict['drawdown']=drwadown
        print(data_dict)
        # 处理policy_2024表（汇率政策）
        currency1, currency2 = currency_pair
        print(currency1, currency2)
        policy_records = models.policy_2024.objects.filter(
            Date__range=[dates_begin, dates_end]
        ).filter(
            Q(affect_currency__contains=currency1) |
            Q(affect_currency__contains=currency2)
        )
        if policy_records is None:
           print('没东西')
        else:
         data_dict['policy'] = [p.text_vectors for p in policy_records]
         print(data_dict)
        # 处理news_2024表（地缘政治）
        country_query = Q()
        for country in countries:
            country_query |= Q(Countries__contains=country.strip())

        news_records =models.news_2024.objects.filter(
            Date__range=[dates_begin, dates_end]
        ).filter(country_query)
        data_dict['news'] = [n.Content for n in news_records]
        print(data_dict)
        # 处理basic_info_2024表（经济指标）
        basic_records = models.basic_info_2024.objects.filter(
            Date__range=[dates_begin, dates_end],
            currency__in=[currency1, currency2]
        ).values('cpi', 'gdp', 'pmi', 'ppi', 'cci', 'unemployment')

        # 将QuerySet转换为字典列表，并处理字段类型
        formatted_records = []
        for record in basic_records:
            formatted = {k: float(v) if v.replace('.', '', 1).isdigit() else v
                         for k, v in record.items()}
            formatted_records.append(formatted)

        data_dict['basic_info'] = formatted_records
        print(data_dict)


    except Exception as e:
        print(f"Database query error: {str(e)}")
        return {
            'dates_begin': [],
            'dates_end': [],
            'drawdown': [],

            'policy':[],
            'news':[],
            'basic_info':[]
        }

    return data_dict


def generate_query( currency_pair, data_dict,maxdrawdown,identify,flex_rate):
        """
        根据数据库中的数据组织一次提问
        :param currency_pair: 货币对名称
        :param data_dict: 包含从数据库中获取的数据的字典
        :return: 按照模板格式生成的提问
        """
        template = """该货币对名称:{}
        预测风险开始时间:{}
        预测风险结束时间:{}
        当前回撤:{}
        最大回撤:{}
        汇率波动情况:{}
        各国经济指标:{}
        各国汇率政策:{}
        地缘政治因素:{}
        身份信息:{}
        """

        # 按照模板格式生成提问
        query = template.format(
            currency_pair,
            data_dict.get("dates_begin", "无相关数据"),
            data_dict.get("dates_end", "无相关数据"),
            data_dict.get("drawdown", "无相关数据"),
            maxdrawdown,
            flex_rate,
            data_dict.get("policy", "无相关数据"),
            data_dict.get("news", "无相关数据"),
            data_dict.get("basic_info", "无相关数据"),
            identify
        )
        return query

def chat_completions(query):
        """
        调用 OpenAI API 获取回答
        :param query: 提问内容
        :return: 大模型的回答
        """
        client = OpenAI(api_key="sk-e6dca9c023dd455291b4946c5f89e171", base_url="https://api.deepseek.com")


        # 定义回答模板
        response_template = """
        根据以上信息和该货币对在网络上的公开信息，你的任务是从专业的角度分点简要总结该货币对的汇率风险信号，并且注意根据身份信息生成针对不同人群的风险报告。

        要求如下：
        1.不允许在答案中添加编造成分；
        2.引用行业相关术语，突显专业性；
        3.答案请使用中文，字数在700字以内；
        4.将你的回答分点列出，确保逻辑清晰；
        5.使用段落结构，输出的每段文字的首行缩进2个中文字符，段落之间无空行，保持格式整洁美观；
        6.输出格式请严格参照示例的输出格式。
        7.根据不同的身份信息给出具有针对性的报告
        8.给出的建议要切实有效

示例：
人民币兑美元（USD/CNY）汇率风险深度分析报告
一、波动周期分析
根据当前市场数据，人民币兑美元汇率波动率σ处于0.0101至0.1020之间，对应表5的波动性等级为“中”。这表明市场波动性已从较低水平上升至中等水平，预示着汇率风险正在积累。当前回撤已达2.9%，接近您设置的3%的预警线，表明在2024年7月1日至8月1日的风险窗口期内，汇率波动性可能进一步加剧。
二、驱动要素深度解析
1. 经济基本面（注意一定要包含cpi gdp pmi ppi cci unemployment六个维度）
美国经济数据喜忧参半，一季度GDP增长2.0%，但通胀率仍高于2%目标，劳动力市场紧张状况有所缓解，但失业率仍处于历史低位。中国经济一季度GDP增长4.5%，消费和投资有所改善，但出口面临压力，贸易顺差收窄。
2.政策多维博弈
2024年7月12日至14日期间，中国央行与美联储的汇率政策形成鲜明博弈。7月12日，中国外汇交易中心将人民币中间价定为1美元兑7.1315元，当日央行通过增发300亿元离岸央票（含150亿元3个月期、100亿元6个月期），使香港离岸人民币隔夜拆借利率（HIBOR）骤升180个基点至5.8%，有效抑制做空压力，USD/CNH即期汇率稳定在7.15-7.18区间。同期美联储维持联邦基金利率5.5%高位，美债10年期收益率攀升至4.8%，吸引单周超120亿美元国际资本流入美元资产，推动美元指数突破105.5关口。政策对冲下，人民币汇率在7月14日收于7.1620，较政策实施前仅微贬0.3%，展现央地政策精准调控效力。
3.地缘冲击波传导
2024年6月15日至20日期间，全球地缘政治局势复杂多变，显著影响了汇率市场。6月15日，美国商务部将长江存储等12家中企列入实体清单，实施7纳米以下芯片设备禁运，涉及年贸易额58亿美元。禁令发布次日，离岸人民币对美元急贬0.8%，创2023年5月以来最大单日跌幅。台积电随后暂停南京厂扩产计划，导致半导体设备相关货币（新台币/韩元）波动率指数飙升42%。7月1日生效的《通胀削减法案》修订案，将中国产电动汽车电池组件补贴门槛提升至北美产能占比65%，并将光伏组件关税从25%提高至50%，影响年出口额240亿美元。新规公布后三个交易日，人民币对欧元累计贬值1.2%。6月20日，也门胡塞武装袭击红海油轮，导致布伦特原油突破90美元/桶，沙特里亚尔远期合约隐含波动率跳升28%，以色列新谢克尔对美元单周贬值3.7%，加元受益油价上涨对美元升值1.8%，但卢布受制裁升级拖累贬值4.2%。这些事件增加了市场的不确定性，引发汇率市场波动。
三、分层应对策略
  [个人投资者]
  1. 购汇策略：采用"3-5-2"分批操作（7.25购30%、破7.20追50%、7.30保底20%）
  2. 持汇管理：美元现钞占比≤40%，推荐配置工行"双币宝"（保本收益率2.8%）
  3. 留学缴费：优先使用中行"优汇通"锁定6个月汇率（点差优惠15BP）
  [商业银行]
  1. 风险管控：设置三级预警（7.25黄色预警/7.28橙色预警/7.30红色预警）
  2. 产品设计：推出"鲨鱼鳍"结构性存款（执行价7.15-7.35，预期年化3.6-5.2%）
  3. 客户管理：企业客户保证金比例提升至110%（原100%），追加频率每日16:00前
  [跨国企业]
  1. 自然对冲：调整东南亚供应链账期至60天（原90天），匹配82%的应收应付
  2. 金融对冲：买入3个月期7.30看跌期权（权利金0.8%），覆盖65%敞口
  3. 结算优化：对欧贸易采用35%欧元+65%人民币结算，汇损降低0.4个百分点
        """

        # 将提问和回答模板一起发送给大模型
        response = client.chat.completions.create(
            model="deepseek-chat",
            messages=[
                {"role": "system", "content": "You are a helpful master of the foreign exchange market."},
                {"role": "user", "content": query + response_template}
            ]
        )

        try:
            return response.choices[0].message.content
        except TypeError:
            return "服务器发生错误，生成失败"


# 字体配置（使用系统自带字体）
FONT_CONFIG = {
    'font_family': 'SimHei',  # 黑体字体
    'default_font_size': 11,
    'heading_font_size': 14,
    'title_font_size': 18,
    'list_bullet': '• ',
    'list_indent': 15
}

# 样式配置
STYLE_CONFIG = {
    'paragraph': {
        'line_height': 5,
        'space_after': 3
    },
    'heading': {
        'space_after': 10
    },
    'list': {
        'line_height': 6
    }
}


def init_pdf(response):
    """初始化PDF对象并配置基础属性"""
    doc = SimpleDocTemplate(response, pagesize=A4)
    styles = getSampleStyleSheet()
    doc.addFont('SimHei', 'SimHei', 'SimHei.ttf')
    # 定义自定义样式
    styles.add(
        ParagraphStyle(name='TitleStyle', fontSize=FONT_CONFIG['title_font_size'], fontName=FONT_CONFIG['font_family'],
                       leading=24))
    styles.add(ParagraphStyle(name='HeadingStyle', fontSize=FONT_CONFIG['heading_font_size'],
                              fontName=FONT_CONFIG['font_family'], leading=20))
    styles.add(
        ParagraphStyle(name='BodyStyle', fontSize=FONT_CONFIG['default_font_size'], fontName=FONT_CONFIG['font_family'],
                       leading=18))
    styles.add(ParagraphStyle(name='ListStyle', fontSize=FONT_CONFIG['default_font_size'] - 1,
                              fontName=FONT_CONFIG['font_family'], leftIndent=FONT_CONFIG['list_indent']))

    return doc, styles


def process_line(line, current_paragraph, blank_line_count):
    """处理单行文本并更新状态"""
    line = line.strip()

    # 处理空行
    if not line:
        blank_line_count[0] += 1
        if blank_line_count[0] >= 2:
            return True, 'paragraph', None  # 表示需要刷新段落
        return False, None, None

    blank_line_count[0] = 0

    # 识别标题
    if re.match(r'^#{1,3} ', line):
        level = line.count('#')
        header_text = re.sub(r'^#+\s*', '', line)
        return True, 'heading', {'level': level, 'text': header_text}

    # 识别列表项
    if re.match(r'^(\*|•|→)\s', line):
        text = re.sub(r'^(\*|•|→)\s*', '', line)
        return True, 'list', {'text': text}

    # 普通文本（累积段落）
    current_paragraph.append(line)
    return False, None, None


def auto_render(doc, styles, text):
    """自动渲染文本内容"""
    content = []
    current_paragraph = []
    blank_line_count = [0]  # 使用可变对象来保持状态

    for line in text.split('\n'):
        need_flush, element_type, element_data = process_line(line, current_paragraph, blank_line_count)

        if need_flush:
            if element_type == 'paragraph':
                if current_paragraph:
                    text = ' '.join(current_paragraph)
                    content.append(Paragraph(text, styles['BodyStyle']))
                    content.append(Spacer(1, STYLE_CONFIG['paragraph']['space_after']))
                    current_paragraph = []
            elif element_type == 'heading':
                header_style = ParagraphStyle(
                    'HeadingStyle',
                    fontSize=FONT_CONFIG['heading_font_size'] - 2 * element_data['level'],
                    fontName=FONT_CONFIG['font_family'],
                    leading=20 - 2 * element_data['level']
                )
                content.append(Paragraph(element_data['text'], header_style))
                content.append(Spacer(1, STYLE_CONFIG['heading']['space_after']))
            elif element_type == 'list':
                list_style = ParagraphStyle(
                    'ListStyle',
                    leftIndent=FONT_CONFIG['list_indent'],
                    fontName=FONT_CONFIG['font_family'],
                    fontSize=FONT_CONFIG['default_font_size'] - 1
                )
                content.append(Paragraph(FONT_CONFIG['list_bullet'] + element_data['text'], list_style))
                content.append(Spacer(1, STYLE_CONFIG['list']['line_height']))
            else:
                if current_paragraph:
                    text = ' '.join(current_paragraph)
                    content.append(Paragraph(text, styles['BodyStyle']))
                    content.append(Spacer(1, STYLE_CONFIG['paragraph']['space_after']))
                    current_paragraph = []

    # 输出最后未处理的段落
    if current_paragraph:
        text = ' '.join(current_paragraph)
        content.append(Paragraph(text, styles['BodyStyle']))

    return content


def generate_smart_pdf(request):
   if request.method=='GET':
    raw_text = """
    人民币兑美元（USD/CNY）汇率分析报告

    # 核心数据

    当前汇率：7.18\n\n
    波动范围：7.15-7.25\n\n\n

    主要特征：
    • 日均波动率0.68%\n
    → 年化波动率12.5%\n
    ※ 最大回撤2.9%\n\n\n

    ## 风险预警
    重点关注以下指标：\n\n
    1. 离岸在岸价差\n
    2. 期权隐含波动率\n\n\n
    3. 外汇占款变动
    """

    # 创建一个HTTP响应，内容类型为PDF
    response = HttpResponse(content_type='application/pdf')
    response['Content-Disposition'] = 'attachment; filename="smart_report.pdf"'

    # 初始化PDF和样式
    doc, styles = init_pdf(response)
    print('doc' + str(doc), styles)
    # 添加标题
    title = Paragraph("人民币兑美元（USD/CNY）汇率风险深度分析报告", styles['TitleStyle'])
    print('title')
    content = [title, Spacer(1, 0.5 * inch)]
    print(content)
    # 渲染内容
    content += auto_render(doc, styles, raw_text)
    print(content)
    # 构建PDF
    doc.build(content)

    return response