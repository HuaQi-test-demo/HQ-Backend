import json
import string
from dbm import error
import secrets
from os import access

from django.http import JsonResponse
from django.shortcuts import render,HttpResponse,redirect
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

def table(request):
    table_account_name=request.session['account_name']
    if table_account_name is not None :
      print(table_account_name)
      return render(request,'table.html',{'table_account_name':table_account_name})
    else:
        return render(request,'login.html')

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

def select_twe_countries(request):
    if request.method == 'POST':
        try:
            # 获取前端发送的 JSON 数据
            data = json.loads(request.body)
            country_1 = data.get('country_1')
            country_2 = data.get('country_2')
            date_start = data.get('date_start')
            date_end = data.get('date_end')
            eurozone_countries = [
                "Austria", "Belgium", "Croatia", "Cyprus", "Estonia", "Finland", "France",
                "Germany", "Greece", "Ireland", "Italy", "Latvia", "Lithuania", "Luxembourg",
                "Malta", "Netherlands", "Portugal", "Slovakia", "Slovenia", "Spain"
            ]
            if country_1  in eurozone_countries and country_2 in eurozone_countries:
                return JsonResponse({'status': 'error', 'message': '两个欧元国家'})
            else:
                currency_1 = models.country_currency.objects.filter(country=country_1).first().currency
                currency_2 = models.country_currency.objects.filter(country=country_2).first().currency
                obj = models.date_currency_rate.objects.filter(currency_1=currency_1,currency_2=currency_2,date_gte=date_start,date_lte=date_end)
                return JsonResponse({'status': 'correct', 'message': '获取成功','data':{'dates':obj.values_list('date', flat=True),'rates':obj.values_list('rate', flat=True)}})
              
        except json.JSONDecodeError:
            return JsonResponse({'status': 'error', 'message': '无效的 JSON 数据'}, status=400)
        except Exception as e:
            return JsonResponse({'status': 'error', 'message': str(e)}, status=500)
def multi_currency(request):
     if request.method == 'POST':
        try:
            # 解析请求体中的 JSON 数据
            data = json.loads(request.body)
            max_drawdown = data.get("max_drawdown")
            dates = data.get('dates')
            # dates='2024-08-01'
            # max_drawdown=-0.5
            # print(dates,max_drawdown)
            # 查询数据库中指定日期的记录
            queryset = models.ProcessedPreDrawdown.objects.filter(Date=dates)

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
            print(result)
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
                        existing_edge_ab = next((edge for edge in result['edges'] if edge['sourceID'] == currency_a and edge['targetID'] == currency_b), None)
                        existing_edge_ba = next((edge for edge in result['edges'] if edge['sourceID'] == currency_b and edge['targetID'] == currency_a), None)

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
            # print(result)
            #
            #
            # save_path = r'F:\GCN3.17\5_years\result.json'
            #
            #
            # with open(save_path, 'w') as json_file:
            #    json.dump(result, json_file, indent=4)


            # print(f"JSON 文件已保存到：{save_path}")

            return JsonResponse(result)
        except Exception as e:
            return JsonResponse({"error": str(e)}, status=400)
     else:
        return JsonResponse({"error": "Invalid request method"}, status=405)