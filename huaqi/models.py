from contextlib import nullcontext

from django.db import models


# Create your models here.
class userInfo(models.Model):
    name = models.CharField(max_length=100)
    account_name = models.CharField(max_length=100, default='尊贵的用户')
    email = models.EmailField()
    password = models.CharField(max_length=100)
    user_type = models.CharField(max_length=100)


class earth_rate(models.Model):
    date_time = models.DateField()
    country = models.CharField(max_length=100)
    currency = models.CharField(max_length=100)
    currency_sign = models.CharField(max_length=100)
    currency1_name = models.CharField(max_length=100)
    currency_rate1 = models.DecimalField(max_digits=10, decimal_places=6)
    currency2_name = models.CharField(max_length=100)
    currency_rate2 = models.DecimalField(max_digits=10, decimal_places=6)
    currency3_name = models.CharField(max_length=100)
    currency_rate3 = models.DecimalField(max_digits=10, decimal_places=6)
    currency4_name = models.CharField(max_length=100)
    currency_rate4 = models.DecimalField(max_digits=10, decimal_places=6)
    currency5_name = models.CharField(max_length=100)
    currency_rate5 = models.DecimalField(max_digits=10, decimal_places=6)
    currency6_name = models.CharField(max_length=100)
    currency_rate6 = models.DecimalField(max_digits=10, decimal_places=6)
    currency7_name = models.CharField(max_length=100)
    currency_rate7 = models.DecimalField(max_digits=10, decimal_places=6)
    currency8_name = models.CharField(max_length=100)
    currency_rate8 = models.DecimalField(max_digits=10, decimal_places=6)
    currency9_name = models.CharField(max_length=100, null=True, blank=True)
    currency_rate9 = models.DecimalField(max_digits=10, decimal_places=6, null=True, blank=True)


class country_currency(models.Model):
    country = models.CharField(max_length=100)
    currency = models.CharField(max_length=100)


class date_currency_rate(models.Model):
    date = models.CharField(max_length=100)
    currency_1 = models.CharField(max_length=100)
    currency_2 = models.CharField(max_length=100)
    rate = models.DecimalField(max_digits=10, decimal_places=6)


class ProcessedPreDrawdown(models.Model):
    Date=models.DateField(default=str(2000-0-1))
    aed_aed = models.FloatField(db_column='AED_AED', blank=True, null=True)  # Field name made lowercase.
    aed_ars = models.FloatField(db_column='AED_ARS', blank=True, null=True)  # Field name made lowercase.
    aed_aud = models.FloatField(db_column='AED_AUD', blank=True, null=True)  # Field name made lowercase.
    aed_brl = models.FloatField(db_column='AED_BRL', blank=True, null=True)  # Field name made lowercase.
    aed_cad = models.FloatField(db_column='AED_CAD', blank=True, null=True)  # Field name made lowercase.
    aed_chf = models.FloatField(db_column='AED_CHF', blank=True, null=True)  # Field name made lowercase.
    aed_cny = models.FloatField(db_column='AED_CNY', blank=True, null=True)  # Field name made lowercase.
    aed_eur = models.FloatField(db_column='AED_EUR', blank=True, null=True)  # Field name made lowercase.
    aed_gbp = models.FloatField(db_column='AED_GBP', blank=True, null=True)  # Field name made lowercase.
    aed_idr = models.FloatField(db_column='AED_IDR', blank=True, null=True)  # Field name made lowercase.
    aed_ils = models.FloatField(db_column='AED_ILS', blank=True, null=True)  # Field name made lowercase.
    aed_inr = models.FloatField(db_column='AED_INR', blank=True, null=True)  # Field name made lowercase.
    aed_jpy = models.FloatField(db_column='AED_JPY', blank=True, null=True)  # Field name made lowercase.
    aed_krw = models.FloatField(db_column='AED_KRW', blank=True, null=True)  # Field name made lowercase.
    aed_mxn = models.FloatField(db_column='AED_MXN', blank=True, null=True)  # Field name made lowercase.
    aed_nok = models.FloatField(db_column='AED_NOK', blank=True, null=True)  # Field name made lowercase.
    aed_pln = models.FloatField(db_column='AED_PLN', blank=True, null=True)  # Field name made lowercase.
    aed_rub = models.FloatField(db_column='AED_RUB', blank=True, null=True)  # Field name made lowercase.
    aed_sar = models.FloatField(db_column='AED_SAR', blank=True, null=True)  # Field name made lowercase.
    aed_sek = models.FloatField(db_column='AED_SEK', blank=True, null=True)  # Field name made lowercase.
    aed_thb = models.FloatField(db_column='AED_THB', blank=True, null=True)  # Field name made lowercase.
    aed_try = models.FloatField(db_column='AED_TRY', blank=True, null=True)  # Field name made lowercase.
    aed_usd = models.FloatField(db_column='AED_USD', blank=True, null=True)  # Field name made lowercase.
    ars_ars = models.FloatField(db_column='ARS_ARS', blank=True, null=True)  # Field name made lowercase.
    ars_aud = models.FloatField(db_column='ARS_AUD', blank=True, null=True)  # Field name made lowercase.
    ars_brl = models.FloatField(db_column='ARS_BRL', blank=True, null=True)  # Field name made lowercase.
    ars_cad = models.FloatField(db_column='ARS_CAD', blank=True, null=True)  # Field name made lowercase.
    ars_chf = models.FloatField(db_column='ARS_CHF', blank=True, null=True)  # Field name made lowercase.
    ars_cny = models.FloatField(db_column='ARS_CNY', blank=True, null=True)  # Field name made lowercase.
    ars_eur = models.FloatField(db_column='ARS_EUR', blank=True, null=True)  # Field name made lowercase.
    ars_gbp = models.FloatField(db_column='ARS_GBP', blank=True, null=True)  # Field name made lowercase.
    ars_idr = models.FloatField(db_column='ARS_IDR', blank=True, null=True)  # Field name made lowercase.
    ars_ils = models.FloatField(db_column='ARS_ILS', blank=True, null=True)  # Field name made lowercase.
    ars_inr = models.FloatField(db_column='ARS_INR', blank=True, null=True)  # Field name made lowercase.
    ars_jpy = models.FloatField(db_column='ARS_JPY', blank=True, null=True)  # Field name made lowercase.
    ars_krw = models.FloatField(db_column='ARS_KRW', blank=True, null=True)  # Field name made lowercase.
    ars_mxn = models.FloatField(db_column='ARS_MXN', blank=True, null=True)  # Field name made lowercase.
    ars_nok = models.FloatField(db_column='ARS_NOK', blank=True, null=True)  # Field name made lowercase.
    ars_pln = models.FloatField(db_column='ARS_PLN', blank=True, null=True)  # Field name made lowercase.
    ars_rub = models.FloatField(db_column='ARS_RUB', blank=True, null=True)  # Field name made lowercase.
    ars_sar = models.FloatField(db_column='ARS_SAR', blank=True, null=True)  # Field name made lowercase.
    ars_sek = models.FloatField(db_column='ARS_SEK', blank=True, null=True)  # Field name made lowercase.
    ars_thb = models.FloatField(db_column='ARS_THB', blank=True, null=True)  # Field name made lowercase.
    ars_try = models.FloatField(db_column='ARS_TRY', blank=True, null=True)  # Field name made lowercase.
    ars_usd = models.FloatField(db_column='ARS_USD', blank=True, null=True)  # Field name made lowercase.
    aud_aud = models.FloatField(db_column='AUD_AUD', blank=True, null=True)  # Field name made lowercase.
    aud_brl = models.FloatField(db_column='AUD_BRL', blank=True, null=True)  # Field name made lowercase.
    aud_cad = models.FloatField(db_column='AUD_CAD', blank=True, null=True)  # Field name made lowercase.
    aud_chf = models.FloatField(db_column='AUD_CHF', blank=True, null=True)  # Field name made lowercase.
    aud_cny = models.FloatField(db_column='AUD_CNY', blank=True, null=True)  # Field name made lowercase.
    aud_eur = models.FloatField(db_column='AUD_EUR', blank=True, null=True)  # Field name made lowercase.
    aud_gbp = models.FloatField(db_column='AUD_GBP', blank=True, null=True)  # Field name made lowercase.
    aud_idr = models.FloatField(db_column='AUD_IDR', blank=True, null=True)  # Field name made lowercase.
    aud_ils = models.FloatField(db_column='AUD_ILS', blank=True, null=True)  # Field name made lowercase.
    aud_inr = models.FloatField(db_column='AUD_INR', blank=True, null=True)  # Field name made lowercase.
    aud_jpy = models.FloatField(db_column='AUD_JPY', blank=True, null=True)  # Field name made lowercase.
    aud_krw = models.FloatField(db_column='AUD_KRW', blank=True, null=True)  # Field name made lowercase.
    aud_mxn = models.FloatField(db_column='AUD_MXN', blank=True, null=True)  # Field name made lowercase.
    aud_nok = models.FloatField(db_column='AUD_NOK', blank=True, null=True)  # Field name made lowercase.
    aud_pln = models.FloatField(db_column='AUD_PLN', blank=True, null=True)  # Field name made lowercase.
    aud_rub = models.FloatField(db_column='AUD_RUB', blank=True, null=True)  # Field name made lowercase.
    aud_sar = models.FloatField(db_column='AUD_SAR', blank=True, null=True)  # Field name made lowercase.
    aud_sek = models.FloatField(db_column='AUD_SEK', blank=True, null=True)  # Field name made lowercase.
    aud_thb = models.FloatField(db_column='AUD_THB', blank=True, null=True)  # Field name made lowercase.
    aud_try = models.FloatField(db_column='AUD_TRY', blank=True, null=True)  # Field name made lowercase.
    aud_usd = models.FloatField(db_column='AUD_USD', blank=True, null=True)  # Field name made lowercase.
    brl_brl = models.FloatField(db_column='BRL_BRL', blank=True, null=True)  # Field name made lowercase.
    brl_cad = models.FloatField(db_column='BRL_CAD', blank=True, null=True)  # Field name made lowercase.
    brl_chf = models.FloatField(db_column='BRL_CHF', blank=True, null=True)  # Field name made lowercase.
    brl_cny = models.FloatField(db_column='BRL_CNY', blank=True, null=True)  # Field name made lowercase.
    brl_eur = models.FloatField(db_column='BRL_EUR', blank=True, null=True)  # Field name made lowercase.
    brl_gbp = models.FloatField(db_column='BRL_GBP', blank=True, null=True)  # Field name made lowercase.
    brl_idr = models.FloatField(db_column='BRL_IDR', blank=True, null=True)  # Field name made lowercase.
    brl_ils = models.FloatField(db_column='BRL_ILS', blank=True, null=True)  # Field name made lowercase.
    brl_inr = models.FloatField(db_column='BRL_INR', blank=True, null=True)  # Field name made lowercase.
    brl_jpy = models.FloatField(db_column='BRL_JPY', blank=True, null=True)  # Field name made lowercase.
    brl_krw = models.FloatField(db_column='BRL_KRW', blank=True, null=True)  # Field name made lowercase.
    brl_mxn = models.FloatField(db_column='BRL_MXN', blank=True, null=True)  # Field name made lowercase.
    brl_nok = models.FloatField(db_column='BRL_NOK', blank=True, null=True)  # Field name made lowercase.
    brl_pln = models.FloatField(db_column='BRL_PLN', blank=True, null=True)  # Field name made lowercase.
    brl_rub = models.FloatField(db_column='BRL_RUB', blank=True, null=True)  # Field name made lowercase.
    brl_sar = models.FloatField(db_column='BRL_SAR', blank=True, null=True)  # Field name made lowercase.
    brl_sek = models.FloatField(db_column='BRL_SEK', blank=True, null=True)  # Field name made lowercase.
    brl_thb = models.FloatField(db_column='BRL_THB', blank=True, null=True)  # Field name made lowercase.
    brl_try = models.FloatField(db_column='BRL_TRY', blank=True, null=True)  # Field name made lowercase.
    brl_usd = models.FloatField(db_column='BRL_USD', blank=True, null=True)  # Field name made lowercase.
    cad_cad = models.FloatField(db_column='CAD_CAD', blank=True, null=True)  # Field name made lowercase.
    cad_chf = models.FloatField(db_column='CAD_CHF', blank=True, null=True)  # Field name made lowercase.
    cad_cny = models.FloatField(db_column='CAD_CNY', blank=True, null=True)  # Field name made lowercase.
    cad_eur = models.FloatField(db_column='CAD_EUR', blank=True, null=True)  # Field name made lowercase.
    cad_gbp = models.FloatField(db_column='CAD_GBP', blank=True, null=True)  # Field name made lowercase.
    cad_idr = models.FloatField(db_column='CAD_IDR', blank=True, null=True)  # Field name made lowercase.
    cad_ils = models.FloatField(db_column='CAD_ILS', blank=True, null=True)  # Field name made lowercase.
    cad_inr = models.FloatField(db_column='CAD_INR', blank=True, null=True)  # Field name made lowercase.
    cad_jpy = models.FloatField(db_column='CAD_JPY', blank=True, null=True)  # Field name made lowercase.
    cad_krw = models.FloatField(db_column='CAD_KRW', blank=True, null=True)  # Field name made lowercase.
    cad_mxn = models.FloatField(db_column='CAD_MXN', blank=True, null=True)  # Field name made lowercase.
    cad_nok = models.FloatField(db_column='CAD_NOK', blank=True, null=True)  # Field name made lowercase.
    cad_pln = models.FloatField(db_column='CAD_PLN', blank=True, null=True)  # Field name made lowercase.
    cad_rub = models.FloatField(db_column='CAD_RUB', blank=True, null=True)  # Field name made lowercase.
    cad_sar = models.FloatField(db_column='CAD_SAR', blank=True, null=True)  # Field name made lowercase.
    cad_sek = models.FloatField(db_column='CAD_SEK', blank=True, null=True)  # Field name made lowercase.
    cad_thb = models.FloatField(db_column='CAD_THB', blank=True, null=True)  # Field name made lowercase.
    cad_try = models.FloatField(db_column='CAD_TRY', blank=True, null=True)  # Field name made lowercase.
    cad_usd = models.FloatField(db_column='CAD_USD', blank=True, null=True)  # Field name made lowercase.
    chf_chf = models.FloatField(db_column='CHF_CHF', blank=True, null=True)  # Field name made lowercase.
    chf_cny = models.FloatField(db_column='CHF_CNY', blank=True, null=True)  # Field name made lowercase.
    chf_eur = models.FloatField(db_column='CHF_EUR', blank=True, null=True)  # Field name made lowercase.
    chf_gbp = models.FloatField(db_column='CHF_GBP', blank=True, null=True)  # Field name made lowercase.
    chf_idr = models.FloatField(db_column='CHF_IDR', blank=True, null=True)  # Field name made lowercase.
    chf_ils = models.FloatField(db_column='CHF_ILS', blank=True, null=True)  # Field name made lowercase.
    chf_inr = models.FloatField(db_column='CHF_INR', blank=True, null=True)  # Field name made lowercase.
    chf_jpy = models.FloatField(db_column='CHF_JPY', blank=True, null=True)  # Field name made lowercase.
    chf_krw = models.FloatField(db_column='CHF_KRW', blank=True, null=True)  # Field name made lowercase.
    chf_mxn = models.FloatField(db_column='CHF_MXN', blank=True, null=True)  # Field name made lowercase.
    chf_nok = models.FloatField(db_column='CHF_NOK', blank=True, null=True)  # Field name made lowercase.
    chf_pln = models.FloatField(db_column='CHF_PLN', blank=True, null=True)  # Field name made lowercase.
    chf_rub = models.FloatField(db_column='CHF_RUB', blank=True, null=True)  # Field name made lowercase.
    chf_sar = models.FloatField(db_column='CHF_SAR', blank=True, null=True)  # Field name made lowercase.
    chf_sek = models.FloatField(db_column='CHF_SEK', blank=True, null=True)  # Field name made lowercase.
    chf_thb = models.FloatField(db_column='CHF_THB', blank=True, null=True)  # Field name made lowercase.
    chf_try = models.FloatField(db_column='CHF_TRY', blank=True, null=True)  # Field name made lowercase.
    chf_usd = models.FloatField(db_column='CHF_USD', blank=True, null=True)  # Field name made lowercase.
    cny_cny = models.FloatField(db_column='CNY_CNY', blank=True, null=True)  # Field name made lowercase.
    cny_eur = models.FloatField(db_column='CNY_EUR', blank=True, null=True)  # Field name made lowercase.
    cny_gbp = models.FloatField(db_column='CNY_GBP', blank=True, null=True)  # Field name made lowercase.
    cny_idr = models.FloatField(db_column='CNY_IDR', blank=True, null=True)  # Field name made lowercase.
    cny_ils = models.FloatField(db_column='CNY_ILS', blank=True, null=True)  # Field name made lowercase.
    cny_inr = models.FloatField(db_column='CNY_INR', blank=True, null=True)  # Field name made lowercase.
    cny_jpy = models.FloatField(db_column='CNY_JPY', blank=True, null=True)  # Field name made lowercase.
    cny_krw = models.FloatField(db_column='CNY_KRW', blank=True, null=True)  # Field name made lowercase.
    cny_mxn = models.FloatField(db_column='CNY_MXN', blank=True, null=True)  # Field name made lowercase.
    cny_nok = models.FloatField(db_column='CNY_NOK', blank=True, null=True)  # Field name made lowercase.
    cny_pln = models.FloatField(db_column='CNY_PLN', blank=True, null=True)  # Field name made lowercase.
    cny_rub = models.FloatField(db_column='CNY_RUB', blank=True, null=True)  # Field name made lowercase.
    cny_sar = models.FloatField(db_column='CNY_SAR', blank=True, null=True)  # Field name made lowercase.
    cny_sek = models.FloatField(db_column='CNY_SEK', blank=True, null=True)  # Field name made lowercase.
    cny_thb = models.FloatField(db_column='CNY_THB', blank=True, null=True)  # Field name made lowercase.
    cny_try = models.FloatField(db_column='CNY_TRY', blank=True, null=True)  # Field name made lowercase.
    cny_usd = models.FloatField(db_column='CNY_USD', blank=True, null=True)  # Field name made lowercase.
    eur_eur = models.FloatField(db_column='EUR_EUR', blank=True, null=True)  # Field name made lowercase.
    eur_gbp = models.FloatField(db_column='EUR_GBP', blank=True, null=True)  # Field name made lowercase.
    eur_idr = models.FloatField(db_column='EUR_IDR', blank=True, null=True)  # Field name made lowercase.
    eur_ils = models.FloatField(db_column='EUR_ILS', blank=True, null=True)  # Field name made lowercase.
    eur_inr = models.FloatField(db_column='EUR_INR', blank=True, null=True)  # Field name made lowercase.
    eur_jpy = models.FloatField(db_column='EUR_JPY', blank=True, null=True)  # Field name made lowercase.
    eur_krw = models.FloatField(db_column='EUR_KRW', blank=True, null=True)  # Field name made lowercase.
    eur_mxn = models.FloatField(db_column='EUR_MXN', blank=True, null=True)  # Field name made lowercase.
    eur_nok = models.FloatField(db_column='EUR_NOK', blank=True, null=True)  # Field name made lowercase.
    eur_pln = models.FloatField(db_column='EUR_PLN', blank=True, null=True)  # Field name made lowercase.
    eur_rub = models.FloatField(db_column='EUR_RUB', blank=True, null=True)  # Field name made lowercase.
    eur_sar = models.FloatField(db_column='EUR_SAR', blank=True, null=True)  # Field name made lowercase.
    eur_sek = models.FloatField(db_column='EUR_SEK', blank=True, null=True)  # Field name made lowercase.
    eur_thb = models.FloatField(db_column='EUR_THB', blank=True, null=True)  # Field name made lowercase.
    eur_try = models.FloatField(db_column='EUR_TRY', blank=True, null=True)  # Field name made lowercase.
    eur_usd = models.FloatField(db_column='EUR_USD', blank=True, null=True)  # Field name made lowercase.
    gbp_gbp = models.FloatField(db_column='GBP_GBP', blank=True, null=True)  # Field name made lowercase.
    gbp_idr = models.FloatField(db_column='GBP_IDR', blank=True, null=True)  # Field name made lowercase.
    gbp_ils = models.FloatField(db_column='GBP_ILS', blank=True, null=True)  # Field name made lowercase.
    gbp_inr = models.FloatField(db_column='GBP_INR', blank=True, null=True)  # Field name made lowercase.
    gbp_jpy = models.FloatField(db_column='GBP_JPY', blank=True, null=True)  # Field name made lowercase.
    gbp_krw = models.FloatField(db_column='GBP_KRW', blank=True, null=True)  # Field name made lowercase.
    gbp_mxn = models.FloatField(db_column='GBP_MXN', blank=True, null=True)  # Field name made lowercase.
    gbp_nok = models.FloatField(db_column='GBP_NOK', blank=True, null=True)  # Field name made lowercase.
    gbp_pln = models.FloatField(db_column='GBP_PLN', blank=True, null=True)  # Field name made lowercase.
    gbp_rub = models.FloatField(db_column='GBP_RUB', blank=True, null=True)  # Field name made lowercase.
    gbp_sar = models.FloatField(db_column='GBP_SAR', blank=True, null=True)  # Field name made lowercase.
    gbp_sek = models.FloatField(db_column='GBP_SEK', blank=True, null=True)  # Field name made lowercase.
    gbp_thb = models.FloatField(db_column='GBP_THB', blank=True, null=True)  # Field name made lowercase.
    gbp_try = models.FloatField(db_column='GBP_TRY', blank=True, null=True)  # Field name made lowercase.
    gbp_usd = models.FloatField(db_column='GBP_USD', blank=True, null=True)  # Field name made lowercase.
    idr_idr = models.FloatField(db_column='IDR_IDR', blank=True, null=True)  # Field name made lowercase.
    idr_ils = models.FloatField(db_column='IDR_ILS', blank=True, null=True)  # Field name made lowercase.
    idr_inr = models.FloatField(db_column='IDR_INR', blank=True, null=True)  # Field name made lowercase.
    idr_jpy = models.FloatField(db_column='IDR_JPY', blank=True, null=True)  # Field name made lowercase.
    idr_krw = models.FloatField(db_column='IDR_KRW', blank=True, null=True)  # Field name made lowercase.
    idr_mxn = models.FloatField(db_column='IDR_MXN', blank=True, null=True)  # Field name made lowercase.
    idr_nok = models.FloatField(db_column='IDR_NOK', blank=True, null=True)  # Field name made lowercase.
    idr_pln = models.FloatField(db_column='IDR_PLN', blank=True, null=True)  # Field name made lowercase.
    idr_rub = models.FloatField(db_column='IDR_RUB', blank=True, null=True)  # Field name made lowercase.
    idr_sar = models.FloatField(db_column='IDR_SAR', blank=True, null=True)  # Field name made lowercase.
    idr_sek = models.FloatField(db_column='IDR_SEK', blank=True, null=True)  # Field name made lowercase.
    idr_thb = models.FloatField(db_column='IDR_THB', blank=True, null=True)  # Field name made lowercase.
    idr_try = models.FloatField(db_column='IDR_TRY', blank=True, null=True)  # Field name made lowercase.
    idr_usd = models.FloatField(db_column='IDR_USD', blank=True, null=True)  # Field name made lowercase.
    ils_ils = models.FloatField(db_column='ILS_ILS', blank=True, null=True)  # Field name made lowercase.
    ils_inr = models.FloatField(db_column='ILS_INR', blank=True, null=True)  # Field name made lowercase.
    ils_jpy = models.FloatField(db_column='ILS_JPY', blank=True, null=True)  # Field name made lowercase.
    ils_krw = models.FloatField(db_column='ILS_KRW', blank=True, null=True)  # Field name made lowercase.
    ils_mxn = models.FloatField(db_column='ILS_MXN', blank=True, null=True)  # Field name made lowercase.
    ils_nok = models.FloatField(db_column='ILS_NOK', blank=True, null=True)  # Field name made lowercase.
    ils_pln = models.FloatField(db_column='ILS_PLN', blank=True, null=True)  # Field name made lowercase.
    ils_rub = models.FloatField(db_column='ILS_RUB', blank=True, null=True)  # Field name made lowercase.
    ils_sar = models.FloatField(db_column='ILS_SAR', blank=True, null=True)  # Field name made lowercase.
    ils_sek = models.FloatField(db_column='ILS_SEK', blank=True, null=True)  # Field name made lowercase.
    ils_thb = models.FloatField(db_column='ILS_THB', blank=True, null=True)  # Field name made lowercase.
    ils_try = models.FloatField(db_column='ILS_TRY', blank=True, null=True)  # Field name made lowercase.
    ils_usd = models.FloatField(db_column='ILS_USD', blank=True, null=True)  # Field name made lowercase.
    inr_inr = models.FloatField(db_column='INR_INR', blank=True, null=True)  # Field name made lowercase.
    inr_jpy = models.FloatField(db_column='INR_JPY', blank=True, null=True)  # Field name made lowercase.
    inr_krw = models.FloatField(db_column='INR_KRW', blank=True, null=True)  # Field name made lowercase.
    inr_mxn = models.FloatField(db_column='INR_MXN', blank=True, null=True)  # Field name made lowercase.
    inr_nok = models.FloatField(db_column='INR_NOK', blank=True, null=True)  # Field name made lowercase.
    inr_pln = models.FloatField(db_column='INR_PLN', blank=True, null=True)  # Field name made lowercase.
    inr_rub = models.FloatField(db_column='INR_RUB', blank=True, null=True)  # Field name made lowercase.
    inr_sar = models.FloatField(db_column='INR_SAR', blank=True, null=True)  # Field name made lowercase.
    inr_sek = models.FloatField(db_column='INR_SEK', blank=True, null=True)  # Field name made lowercase.
    inr_thb = models.FloatField(db_column='INR_THB', blank=True, null=True)  # Field name made lowercase.
    inr_try = models.FloatField(db_column='INR_TRY', blank=True, null=True)  # Field name made lowercase.
    inr_usd = models.FloatField(db_column='INR_USD', blank=True, null=True)  # Field name made lowercase.
    jpy_jpy = models.FloatField(db_column='JPY_JPY', blank=True, null=True)  # Field name made lowercase.
    jpy_krw = models.FloatField(db_column='JPY_KRW', blank=True, null=True)  # Field name made lowercase.
    jpy_mxn = models.FloatField(db_column='JPY_MXN', blank=True, null=True)  # Field name made lowercase.
    jpy_nok = models.FloatField(db_column='JPY_NOK', blank=True, null=True)  # Field name made lowercase.
    jpy_pln = models.FloatField(db_column='JPY_PLN', blank=True, null=True)  # Field name made lowercase.
    jpy_rub = models.FloatField(db_column='JPY_RUB', blank=True, null=True)  # Field name made lowercase.
    jpy_sar = models.FloatField(db_column='JPY_SAR', blank=True, null=True)  # Field name made lowercase.
    jpy_sek = models.FloatField(db_column='JPY_SEK', blank=True, null=True)  # Field name made lowercase.
    jpy_thb = models.FloatField(db_column='JPY_THB', blank=True, null=True)  # Field name made lowercase.
    jpy_try = models.FloatField(db_column='JPY_TRY', blank=True, null=True)  # Field name made lowercase.
    jpy_usd = models.FloatField(db_column='JPY_USD', blank=True, null=True)  # Field name made lowercase.
    krw_krw = models.FloatField(db_column='KRW_KRW', blank=True, null=True)  # Field name made lowercase.
    krw_mxn = models.FloatField(db_column='KRW_MXN', blank=True, null=True)  # Field name made lowercase.
    krw_nok = models.FloatField(db_column='KRW_NOK', blank=True, null=True)  # Field name made lowercase.
    krw_pln = models.FloatField(db_column='KRW_PLN', blank=True, null=True)  # Field name made lowercase.
    krw_rub = models.FloatField(db_column='KRW_RUB', blank=True, null=True)  # Field name made lowercase.
    krw_sar = models.FloatField(db_column='KRW_SAR', blank=True, null=True)  # Field name made lowercase.
    krw_sek = models.FloatField(db_column='KRW_SEK', blank=True, null=True)  # Field name made lowercase.
    krw_thb = models.FloatField(db_column='KRW_THB', blank=True, null=True)  # Field name made lowercase.
    krw_try = models.FloatField(db_column='KRW_TRY', blank=True, null=True)  # Field name made lowercase.
    krw_usd = models.FloatField(db_column='KRW_USD', blank=True, null=True)  # Field name made lowercase.
    mxn_mxn = models.FloatField(db_column='MXN_MXN', blank=True, null=True)  # Field name made lowercase.
    mxn_nok = models.FloatField(db_column='MXN_NOK', blank=True, null=True)  # Field name made lowercase.
    mxn_pln = models.FloatField(db_column='MXN_PLN', blank=True, null=True)  # Field name made lowercase.
    mxn_rub = models.FloatField(db_column='MXN_RUB', blank=True, null=True)  # Field name made lowercase.
    mxn_sar = models.FloatField(db_column='MXN_SAR', blank=True, null=True)  # Field name made lowercase.
    mxn_sek = models.FloatField(db_column='MXN_SEK', blank=True, null=True)  # Field name made lowercase.
    mxn_thb = models.FloatField(db_column='MXN_THB', blank=True, null=True)  # Field name made lowercase.
    mxn_try = models.FloatField(db_column='MXN_TRY', blank=True, null=True)  # Field name made lowercase.
    mxn_usd = models.FloatField(db_column='MXN_USD', blank=True, null=True)  # Field name made lowercase.
    nok_nok = models.FloatField(db_column='NOK_NOK', blank=True, null=True)  # Field name made lowercase.
    nok_pln = models.FloatField(db_column='NOK_PLN', blank=True, null=True)  # Field name made lowercase.
    nok_rub = models.FloatField(db_column='NOK_RUB', blank=True, null=True)  # Field name made lowercase.
    nok_sar = models.FloatField(db_column='NOK_SAR', blank=True, null=True)  # Field name made lowercase.
    nok_sek = models.FloatField(db_column='NOK_SEK', blank=True, null=True)  # Field name made lowercase.
    nok_thb = models.FloatField(db_column='NOK_THB', blank=True, null=True)  # Field name made lowercase.
    nok_try = models.FloatField(db_column='NOK_TRY', blank=True, null=True)  # Field name made lowercase.
    nok_usd = models.FloatField(db_column='NOK_USD', blank=True, null=True)  # Field name made lowercase.
    pln_pln = models.FloatField(db_column='PLN_PLN', blank=True, null=True)  # Field name made lowercase.
    pln_rub = models.FloatField(db_column='PLN_RUB', blank=True, null=True)  # Field name made lowercase.
    pln_sar = models.FloatField(db_column='PLN_SAR', blank=True, null=True)  # Field name made lowercase.
    pln_sek = models.FloatField(db_column='PLN_SEK', blank=True, null=True)  # Field name made lowercase.
    pln_thb = models.FloatField(db_column='PLN_THB', blank=True, null=True)  # Field name made lowercase.
    pln_try = models.FloatField(db_column='PLN_TRY', blank=True, null=True)  # Field name made lowercase.
    pln_usd = models.FloatField(db_column='PLN_USD', blank=True, null=True)  # Field name made lowercase.
    rub_rub = models.FloatField(db_column='RUB_RUB', blank=True, null=True)  # Field name made lowercase.
    rub_sar = models.FloatField(db_column='RUB_SAR', blank=True, null=True)  # Field name made lowercase.
    rub_sek = models.FloatField(db_column='RUB_SEK', blank=True, null=True)  # Field name made lowercase.
    rub_thb = models.FloatField(db_column='RUB_THB', blank=True, null=True)  # Field name made lowercase.
    rub_try = models.FloatField(db_column='RUB_TRY', blank=True, null=True)  # Field name made lowercase.
    rub_usd = models.FloatField(db_column='RUB_USD', blank=True, null=True)  # Field name made lowercase.
    sar_sar = models.FloatField(db_column='SAR_SAR', blank=True, null=True)  # Field name made lowercase.
    sar_sek = models.FloatField(db_column='SAR_SEK', blank=True, null=True)  # Field name made lowercase.
    sar_thb = models.FloatField(db_column='SAR_THB', blank=True, null=True)  # Field name made lowercase.
    sar_try = models.FloatField(db_column='SAR_TRY', blank=True, null=True)  # Field name made lowercase.
    sar_usd = models.FloatField(db_column='SAR_USD', blank=True, null=True)  # Field name made lowercase.
    sek_sek = models.FloatField(db_column='SEK_SEK', blank=True, null=True)  # Field name made lowercase.
    sek_thb = models.FloatField(db_column='SEK_THB', blank=True, null=True)  # Field name made lowercase.
    sek_try = models.FloatField(db_column='SEK_TRY', blank=True, null=True)  # Field name made lowercase.
    sek_usd = models.FloatField(db_column='SEK_USD', blank=True, null=True)  # Field name made lowercase.
    thb_thb = models.FloatField(db_column='THB_THB', blank=True, null=True)  # Field name made lowercase.
    thb_try = models.FloatField(db_column='THB_TRY', blank=True, null=True)  # Field name made lowercase.
    thb_usd = models.FloatField(db_column='THB_USD', blank=True, null=True)  # Field name made lowercase.
    try_try = models.FloatField(db_column='TRY_TRY', blank=True, null=True)  # Field name made lowercase.
    try_usd = models.FloatField(db_column='TRY_USD', blank=True, null=True)  # Field name made lowercase.
    usd_usd = models.FloatField(db_column='USD_USD', blank=True, null=True)  # Field name made lowercase.
