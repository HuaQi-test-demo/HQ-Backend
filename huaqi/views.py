import json
import string
from dbm import error
import secrets
from os import access
import openai
from django.db.models import Q
from django.db.models.expressions import result
from django.http import JsonResponse
from django.shortcuts import render,HttpResponse,redirect
from openai import OpenAI

from huaqi import models
# Create your views here.
def login(request):

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
         #request.session['account_name'] = obj.account_name
            #print(obj.account_name)
            # redirect('/submit/')
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
        data = json.loads(request.body)
        username = data.get('username')
        password =data.get('password')
        confirm_password =data.get('ConfirmPassword')
        user_type =data.get('category')
        email =data.get('email')
        print(username,password,confirm_password,email)

        if password != confirm_password:
            return JsonResponse({'status': 'error', 'message': '两次密码不一致，请重新设置密码'})
        elif models.userInfo.objects.filter(name=username).exists():
            return JsonResponse({'status': 'error', 'message': '账号已存在，请换一个'})
        else:
         models.userInfo.objects.create(name=username,password=password,user_type=user_type,email=email)
         return JsonResponse({'status': 'ok', 'message': '注册成功'})
        
    # if request.method == "GET":
    #     return render(request, 'register.html')
    # else:
    #     new_username = request.POST['username']
    #     new_password = request.POST['password']
    #     new_confirmpassword = request.POST['confirm-password']
    #     new_user_type = request.POST['user_type']
    #     new_email = request.POST['email']
    #     new_account_name = request.POST['account_name']
    #     if new_password != new_confirmpassword:
    #         return render(request,'register.html',{"error":"两次密码不一致，请重新设置密码"})
    #     elif models.userInfo.objects.filter(name=new_username).exists():
    #         return render(request,'register.html',{"error":"账号已存在，请换一个"})
    #     else:
    #      models.userInfo.objects.create(name=new_username,password=new_password,user_type=new_user_type,email=new_email,account_name=new_account_name)
    #      return redirect('/login/')

# def table(request):
#     table_account_name=request.session['account_name']
#     if table_account_name is not None :
#       print(table_account_name)
#       return render(request,'table.html',{'table_account_name':table_account_name})
#     else:
#         return render(request,'login.html')

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

def currency_pair(request):
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
            deal_year = ''+data.get('investmentPeriod')+'年'
            print(deal_year)
            date_start = data.get('startDate')
            date_end = data.get('endDate')
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
                currency_1 = models.country_currency.objects.filter(country=country_1).first().currency
                currency_2 = models.country_currency.objects.filter(country=country_2).first().currency
                obj = models.date_currency_rates.objects.filter(currency_1=currency_1,currency_2=currency_2,date_time_gte=date_start,date_time_lte=date_end,deal_year=deal_year)
                return JsonResponse({'status': 'correct', 
                                     'message': '获取成功',
                                     'data':{
                                         'date_time':obj.values_list('date_time', flat=True),
                                         'predict_rate':obj.values_list('predict_rate', flat=True),
                                         'true_rate':obj.values_list('true_rate', flat=True)}})
        except json.JSONDecodeError:
            return JsonResponse({'status': 'error', 'message': '无效的 JSON 数据'}, status=400)
        except Exception as e:
            return JsonResponse({'status': 'error', 'message': str(e)}, status=500)
        
def multi_currency(request):
     if request.method == 'POST':
        try:
            # 解析请求体中的 JSON 数据
            data = json.loads(request.body)
            max_drawdown = data.get("maxDrawdown")
            dates = data.get('month')
            print(max_drawdown,dates)
            # dates='2024-08-01'
            # max_drawdown=-0.5
            # print(dates,max_drawdown)
            # 查询数据库中指定日期的记录
            queryset_pre_5 = models.ProcessedPreDrawdown.objects.filter(Date=dates)
            queryset_tar_5=models.ProcessedTarDrawdown.objects.filter(Date=dates)
            result1=find_multi_currency(queryset_pre_5,max_drawdown)
            result2=find_multi_currency(queryset_tar_5,max_drawdown)
            return JsonResponse({'result1':result1,'result2':result2})
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
        #
        #
        # save_path = r'F:\GCN3.17\5_years\result.json'
        #
        #
        # with open(save_path, 'w') as json_file:
        #    json.dump(result, json_file, indent=4)

        # print(f"JSON 文件已保存到：{save_path}")



    # else:
    #     result = {"nodes": "没东西", "edges": '没东西'}
    #
    return result
def deepseek_generate(self,dates_begin,dates_end,currency_pair,countries,drawdown,maxdrawdown,identify):

        # 从数据库中获取数据
        data_dict = self.get_data_from_db(dates_begin,dates_end,currency_pair,countries,drawdown)

        # 根据数据库中的数据组织一次提问
        query = self.generate_query(currency_pair, data_dict,maxdrawdown,identify)

        # 使用大模型进行回答
        response_ai = self.chat_completions(query)
        return JsonResponse({'response':response_ai})
def get_data_from_db(self, dates_begin, dates_end, currency_pair,countries,drwadown):
    data_dict = {}
    try:
        data_dict['dates_begin']=dates_begin
        data_dict['dates_end']=dates_end
        data_dict['drawdown']=drwadown

        # 处理policy_2024表（汇率政策）
        currency1, currency2 = currency_pair.split(',')
        policy_records = models.policy_2024.objects.filter(
            Date__range=[dates_begin, dates_end]
        ).filter(
            Q(affect_currency__contains=currency1) |
            Q(affect_currency__contains=currency2)
        )
        data_dict['policy'] = [p.text_vectors for p in policy_records]

        # 处理news_2024表（地缘政治）
        if isinstance(countries, str):
            countries = countries.split(';')
        country_query = Q()
        for country in countries:
            country_query |= Q(Countries__contains=country.strip())

        news_records =models.news_2024.objects.filter(
            Date__range=[dates_begin, dates_end]
        ).filter(country_query)
        data_dict['news'] = [n.Content for n in news_records]

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


def generate_query(self, currency_pair, data_dict,maxdrawdown,identify):
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
            data_dict.get("policy", "无相关数据"),
            data_dict.get("news", "无相关数据"),
            data_dict.get("basic_info", "无相关数据"),
            identify
        )
        return query

def chat_completions(self, query):
        """
        调用 OpenAI API 获取回答
        :param query: 提问内容
        :return: 大模型的回答
        """
        client = OpenAI(api_key="<DeepSeek API Key>", base_url="https://api.deepseek.com")


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
        输出格式：
       人民币兑美元（USD/CNY）汇率风险深度分析报告
        一、波动周期分析
             ·  当前回撤达{2.9}%，接近您设置的{3}%
                风险窗口：{2024-7-1}至{2024-8-1}

      二、驱动要素深度解析
1. 经济基本面裂变
  ·  通胀剪刀差加剧：美国核心CPI维持3.5%高位（住房项贡献58%），中国PPI连续11个月负增长（-1.4%），创2016年来最长通缩周期
  ·  增长动能分化：美国Q2 GDP季调年率2.4% vs 中国6月制造业PMI 49.0（连续3月收缩）
  ·  利率悬崖效应：中美10年期国债利差-215BP，倒挂幅度超2008金融危机峰值（-189BP），触发跨境套利资本日均流出5.2亿美元

2. 政策多维博弈
  ·  中国央行精准滴灌：
     - MLF连续8周净投放5300亿（利率锚定2.5%）
     - 启动离岸央票增发（500亿规模，期限63天）
     - 窗口指导主要银行将结售汇点差压缩至25BP以内
  ·  美联储双重紧缩：
     - 资产负债表缩减950亿/月（MBS减持上限300亿）
     - 逆回购池维持2.1万亿美元超额流动性
     - 利率点阵图隐含2024年降息空间收窄至25BP
  ·  监管科技升级：外汇局跨境金融区块链平台新增"热钱追踪"模块，实时监控1400余家机构外汇头寸

3. 地缘冲击波传导
  ·  贸易战2.0升级：
     - 电动车关税7月生效（影响240亿美元贸易额）
     - 半导体设备出口新规覆盖28nm以下制程
     - 生物技术投资审查清单扩容至37个领域
  ·  资本暗流涌动：
     - 股票市场：EPFR监测显示47亿美元净流出（主动型基金占比73%）
     - 债券市场：境外机构连续9月减持人民币债券（累计4820亿）
     - 直接投资：Q2对华绿地投资同比下降39%（美国企业降幅达58%）
  ·  货币武器化风险：SWIFT数据显示38个国家增加人民币结算占比，但美元仍主导83%能源交易

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

监测机制：
·  每日跟踪CFETS人民币汇率指数、USDCNY 1M ATM波动率等12项指标
·  当中间价连续3日偏离±1%时，启动跨境融资宏观审慎调节
·  每周更新GARCH模型预测区间（95%置信水平：7.15-7.33）交易机会和风险控制。
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
