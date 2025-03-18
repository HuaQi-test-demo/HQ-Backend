import csv
import os
from django.core.management.base import BaseCommand
from huaqi.models import ProcessedTarDrawdown  # 替换为你的应用名称

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'your_project.settings')

class Command(BaseCommand):
    help = 'Import data from CSV file to huaqi_processedtardrawdown table'

    def add_arguments(self, parser):
        parser.add_argument('csv_file', type=str, help='Path to the CSV file')

    def handle(self, *args, **options):
        csv_file_path = options['csv_file']
        with open(csv_file_path, 'r') as csv_file:
            csv_reader = csv.DictReader(csv_file)
            for row in csv_reader:
                # 创建 ProcessedPreDrawdown 对象
                processed_predrawdown = ProcessedTarDrawdown()

                # 逐个字段赋值
                processed_predrawdown.Date = row['Date'] if row['Date'] else None

                processed_predrawdown.aed_aed = float(row['AED_AED']) if row['AED_AED'] else None
                processed_predrawdown.aed_ars = float(row['AED_ARS']) if row['AED_ARS'] else None
                processed_predrawdown.aed_aud = float(row['AED_AUD']) if row['AED_AUD'] else None
                processed_predrawdown.aed_brl = float(row['AED_BRL']) if row['AED_BRL'] else None
                processed_predrawdown.aed_cad = float(row['AED_CAD']) if row['AED_CAD'] else None
                processed_predrawdown.aed_chf = float(row['AED_CHF']) if row['AED_CHF'] else None
                processed_predrawdown.aed_cny = float(row['AED_CNY']) if row['AED_CNY'] else None
                processed_predrawdown.aed_eur = float(row['AED_EUR']) if row['AED_EUR'] else None
                processed_predrawdown.aed_gbp = float(row['AED_GBP']) if row['AED_GBP'] else None
                processed_predrawdown.aed_idr = float(row['AED_IDR']) if row['AED_IDR'] else None
                processed_predrawdown.aed_ils = float(row['AED_ILS']) if row['AED_ILS'] else None
                processed_predrawdown.aed_inr = float(row['AED_INR']) if row['AED_INR'] else None
                processed_predrawdown.aed_jpy = float(row['AED_JPY']) if row['AED_JPY'] else None
                processed_predrawdown.aed_krw = float(row['AED_KRW']) if row['AED_KRW'] else None
                processed_predrawdown.aed_mxn = float(row['AED_MXN']) if row['AED_MXN'] else None
                processed_predrawdown.aed_nok = float(row['AED_NOK']) if row['AED_NOK'] else None
                processed_predrawdown.aed_pln = float(row['AED_PLN']) if row['AED_PLN'] else None
                processed_predrawdown.aed_rub = float(row['AED_RUB']) if row['AED_RUB'] else None
                processed_predrawdown.aed_sar = float(row['AED_SAR']) if row['AED_SAR'] else None
                processed_predrawdown.aed_sek = float(row['AED_SEK']) if row['AED_SEK'] else None
                processed_predrawdown.aed_thb = float(row['AED_THB']) if row['AED_THB'] else None
                processed_predrawdown.aed_try = float(row['AED_TRY']) if row['AED_TRY'] else None
                processed_predrawdown.aed_usd = float(row['AED_USD']) if row['AED_USD'] else None

                processed_predrawdown.ars_ars = float(row['ARS_ARS']) if row['ARS_ARS'] else None
                processed_predrawdown.ars_aud = float(row['ARS_AUD']) if row['ARS_AUD'] else None
                processed_predrawdown.ars_brl = float(row['ARS_BRL']) if row['ARS_BRL'] else None
                processed_predrawdown.ars_cad = float(row['ARS_CAD']) if row['ARS_CAD'] else None
                processed_predrawdown.ars_chf = float(row['ARS_CHF']) if row['ARS_CHF'] else None
                processed_predrawdown.ars_cny = float(row['ARS_CNY']) if row['ARS_CNY'] else None
                processed_predrawdown.ars_eur = float(row['ARS_EUR']) if row['ARS_EUR'] else None
                processed_predrawdown.ars_gbp = float(row['ARS_GBP']) if row['ARS_GBP'] else None
                processed_predrawdown.ars_idr = float(row['ARS_IDR']) if row['ARS_IDR'] else None
                processed_predrawdown.ars_ils = float(row['ARS_ILS']) if row['ARS_ILS'] else None
                processed_predrawdown.ars_inr = float(row['ARS_INR']) if row['ARS_INR'] else None
                processed_predrawdown.ars_jpy = float(row['ARS_JPY']) if row['ARS_JPY'] else None
                processed_predrawdown.ars_krw = float(row['ARS_KRW']) if row['ARS_KRW'] else None
                processed_predrawdown.ars_mxn = float(row['ARS_MXN']) if row['ARS_MXN'] else None
                processed_predrawdown.ars_nok = float(row['ARS_NOK']) if row['ARS_NOK'] else None
                processed_predrawdown.ars_pln = float(row['ARS_PLN']) if row['ARS_PLN'] else None
                processed_predrawdown.ars_rub = float(row['ARS_RUB']) if row['ARS_RUB'] else None
                processed_predrawdown.ars_sar = float(row['ARS_SAR']) if row['ARS_SAR'] else None
                processed_predrawdown.ars_sek = float(row['ARS_SEK']) if row['ARS_SEK'] else None
                processed_predrawdown.ars_thb = float(row['ARS_THB']) if row['ARS_THB'] else None
                processed_predrawdown.ars_try = float(row['ARS_TRY']) if row['ARS_TRY'] else None
                processed_predrawdown.ars_usd = float(row['ARS_USD']) if row['ARS_USD'] else None

                processed_predrawdown.aud_aud = float(row['AUD_AUD']) if row['AUD_AUD'] else None
                processed_predrawdown.aud_brl = float(row['AUD_BRL']) if row['AUD_BRL'] else None
                processed_predrawdown.aud_cad = float(row['AUD_CAD']) if row['AUD_CAD'] else None
                processed_predrawdown.aud_chf = float(row['AUD_CHF']) if row['AUD_CHF'] else None
                processed_predrawdown.aud_cny = float(row['AUD_CNY']) if row['AUD_CNY'] else None
                processed_predrawdown.aud_eur = float(row['AUD_EUR']) if row['AUD_EUR'] else None
                processed_predrawdown.aud_gbp = float(row['AUD_GBP']) if row['AUD_GBP'] else None
                processed_predrawdown.aud_idr = float(row['AUD_IDR']) if row['AUD_IDR'] else None
                processed_predrawdown.aud_ils = float(row['AUD_ILS']) if row['AUD_ILS'] else None
                processed_predrawdown.aud_inr = float(row['AUD_INR']) if row['AUD_INR'] else None
                processed_predrawdown.aud_jpy = float(row['AUD_JPY']) if row['AUD_JPY'] else None
                processed_predrawdown.aud_krw = float(row['AUD_KRW']) if row['AUD_KRW'] else None
                processed_predrawdown.aud_mxn = float(row['AUD_MXN']) if row['AUD_MXN'] else None
                processed_predrawdown.aud_nok = float(row['AUD_NOK']) if row['AUD_NOK'] else None
                processed_predrawdown.aud_pln = float(row['AUD_PLN']) if row['AUD_PLN'] else None
                processed_predrawdown.aud_rub = float(row['AUD_RUB']) if row['AUD_RUB'] else None
                processed_predrawdown.aud_sar = float(row['AUD_SAR']) if row['AUD_SAR'] else None
                processed_predrawdown.aud_sek = float(row['AUD_SEK']) if row['AUD_SEK'] else None
                processed_predrawdown.aud_thb = float(row['AUD_THB']) if row['AUD_THB'] else None
                processed_predrawdown.aud_try = float(row['AUD_TRY']) if row['AUD_TRY'] else None
                processed_predrawdown.aud_usd = float(row['AUD_USD']) if row['AUD_USD'] else None

                processed_predrawdown.brl_brl = float(row['BRL_BRL']) if row['BRL_BRL'] else None
                processed_predrawdown.brl_cad = float(row['BRL_CAD']) if row['BRL_CAD'] else None
                processed_predrawdown.brl_chf = float(row['BRL_CHF']) if row['BRL_CHF'] else None
                processed_predrawdown.brl_cny = float(row['BRL_CNY']) if row['BRL_CNY'] else None
                processed_predrawdown.brl_eur = float(row['BRL_EUR']) if row['BRL_EUR'] else None
                processed_predrawdown.brl_gbp = float(row['BRL_GBP']) if row['BRL_GBP'] else None
                processed_predrawdown.brl_idr = float(row['BRL_IDR']) if row['BRL_IDR'] else None
                processed_predrawdown.brl_ils = float(row['BRL_ILS']) if row['BRL_ILS'] else None
                processed_predrawdown.brl_inr = float(row['BRL_INR']) if row['BRL_INR'] else None
                processed_predrawdown.brl_jpy = float(row['BRL_JPY']) if row['BRL_JPY'] else None
                processed_predrawdown.brl_krw = float(row['BRL_KRW']) if row['BRL_KRW'] else None
                processed_predrawdown.brl_mxn = float(row['BRL_MXN']) if row['BRL_MXN'] else None
                processed_predrawdown.brl_nok = float(row['BRL_NOK']) if row['BRL_NOK'] else None
                processed_predrawdown.brl_pln = float(row['BRL_PLN']) if row['BRL_PLN'] else None
                processed_predrawdown.brl_rub = float(row['BRL_RUB']) if row['BRL_RUB'] else None
                processed_predrawdown.brl_sar = float(row['BRL_SAR']) if row['BRL_SAR'] else None
                processed_predrawdown.brl_sek = float(row['BRL_SEK']) if row['BRL_SEK'] else None
                processed_predrawdown.brl_thb = float(row['BRL_THB']) if row['BRL_THB'] else None
                processed_predrawdown.brl_try = float(row['BRL_TRY']) if row['BRL_TRY'] else None
                processed_predrawdown.brl_usd = float(row['BRL_USD']) if row['BRL_USD'] else None

                processed_predrawdown.cad_cad = float(row['CAD_CAD']) if row['CAD_CAD'] else None
                processed_predrawdown.cad_chf = float(row['CAD_CHF']) if row['CAD_CHF'] else None
                processed_predrawdown.cad_cny = float(row['CAD_CNY']) if row['CAD_CNY'] else None
                processed_predrawdown.cad_eur = float(row['CAD_EUR']) if row['CAD_EUR'] else None
                processed_predrawdown.cad_gbp = float(row['CAD_GBP']) if row['CAD_GBP'] else None
                processed_predrawdown.cad_idr = float(row['CAD_IDR']) if row['CAD_IDR'] else None
                processed_predrawdown.cad_ils = float(row['CAD_ILS']) if row['CAD_ILS'] else None
                processed_predrawdown.cad_inr = float(row['CAD_INR']) if row['CAD_INR'] else None
                processed_predrawdown.cad_jpy = float(row['CAD_JPY']) if row['CAD_JPY'] else None
                processed_predrawdown.cad_krw = float(row['CAD_KRW']) if row['CAD_KRW'] else None
                processed_predrawdown.cad_mxn = float(row['CAD_MXN']) if row['CAD_MXN'] else None
                processed_predrawdown.cad_nok = float(row['CAD_NOK']) if row['CAD_NOK'] else None
                processed_predrawdown.cad_pln = float(row['CAD_PLN']) if row['CAD_PLN'] else None
                processed_predrawdown.cad_rub = float(row['CAD_RUB']) if row['CAD_RUB'] else None
                processed_predrawdown.cad_sar = float(row['CAD_SAR']) if row['CAD_SAR'] else None
                processed_predrawdown.cad_sek = float(row['CAD_SEK']) if row['CAD_SEK'] else None
                processed_predrawdown.cad_thb = float(row['CAD_THB']) if row['CAD_THB'] else None
                processed_predrawdown.cad_try = float(row['CAD_TRY']) if row['CAD_TRY'] else None
                processed_predrawdown.cad_usd = float(row['CAD_USD']) if row['CAD_USD'] else None

                processed_predrawdown.chf_chf = float(row['CHF_CHF']) if row['CHF_CHF'] else None
                processed_predrawdown.chf_cny = float(row['CHF_CNY']) if row['CHF_CNY'] else None
                processed_predrawdown.chf_eur = float(row['CHF_EUR']) if row['CHF_EUR'] else None
                processed_predrawdown.chf_gbp = float(row['CHF_GBP']) if row['CHF_GBP'] else None
                processed_predrawdown.chf_idr = float(row['CHF_IDR']) if row['CHF_IDR'] else None
                processed_predrawdown.chf_ils = float(row['CHF_ILS']) if row['CHF_ILS'] else None
                processed_predrawdown.chf_inr = float(row['CHF_INR']) if row['CHF_INR'] else None
                processed_predrawdown.chf_jpy = float(row['CHF_JPY']) if row['CHF_JPY'] else None
                processed_predrawdown.chf_krw = float(row['CHF_KRW']) if row['CHF_KRW'] else None
                processed_predrawdown.chf_mxn = float(row['CHF_MXN']) if row['CHF_MXN'] else None
                processed_predrawdown.chf_nok = float(row['CHF_NOK']) if row['CHF_NOK'] else None
                processed_predrawdown.chf_pln = float(row['CHF_PLN']) if row['CHF_PLN'] else None
                processed_predrawdown.chf_rub = float(row['CHF_RUB']) if row['CHF_RUB'] else None
                processed_predrawdown.chf_sar = float(row['CHF_SAR']) if row['CHF_SAR'] else None
                processed_predrawdown.chf_sek = float(row['CHF_SEK']) if row['CHF_SEK'] else None
                processed_predrawdown.chf_thb = float(row['CHF_THB']) if row['CHF_THB'] else None
                processed_predrawdown.chf_try = float(row['CHF_TRY']) if row['CHF_TRY'] else None
                processed_predrawdown.chf_usd = float(row['CHF_USD']) if row['CHF_USD'] else None

                processed_predrawdown.cny_cny = float(row['CNY_CNY']) if row['CNY_CNY'] else None
                processed_predrawdown.cny_eur = float(row['CNY_EUR']) if row['CNY_EUR'] else None
                processed_predrawdown.cny_gbp = float(row['CNY_GBP']) if row['CNY_GBP'] else None
                processed_predrawdown.cny_idr = float(row['CNY_IDR']) if row['CNY_IDR'] else None
                processed_predrawdown.cny_ils = float(row['CNY_ILS']) if row['CNY_ILS'] else None
                processed_predrawdown.cny_inr = float(row['CNY_INR']) if row['CNY_INR'] else None
                processed_predrawdown.cny_jpy = float(row['CNY_JPY']) if row['CNY_JPY'] else None
                processed_predrawdown.cny_krw = float(row['CNY_KRW']) if row['CNY_KRW'] else None
                processed_predrawdown.cny_mxn = float(row['CNY_MXN']) if row['CNY_MXN'] else None
                processed_predrawdown.cny_nok = float(row['CNY_NOK']) if row['CNY_NOK'] else None
                processed_predrawdown.cny_pln = float(row['CNY_PLN']) if row['CNY_PLN'] else None
                processed_predrawdown.cny_rub = float(row['CNY_RUB']) if row['CNY_RUB'] else None
                processed_predrawdown.cny_sar = float(row['CNY_SAR']) if row['CNY_SAR'] else None
                processed_predrawdown.cny_sek = float(row['CNY_SEK']) if row['CNY_SEK'] else None
                processed_predrawdown.cny_thb = float(row['CNY_THB']) if row['CNY_THB'] else None
                processed_predrawdown.cny_try = float(row['CNY_TRY']) if row['CNY_TRY'] else None
                processed_predrawdown.cny_usd = float(row['CNY_USD']) if row['CNY_USD'] else None

                processed_predrawdown.eur_eur = float(row['EUR_EUR']) if row['EUR_EUR'] else None
                processed_predrawdown.eur_gbp = float(row['EUR_GBP']) if row['EUR_GBP'] else None
                processed_predrawdown.eur_idr = float(row['EUR_IDR']) if row['EUR_IDR'] else None
                processed_predrawdown.eur_ils = float(row['EUR_ILS']) if row['EUR_ILS'] else None
                processed_predrawdown.eur_inr = float(row['EUR_INR']) if row['EUR_INR'] else None
                processed_predrawdown.eur_jpy = float(row['EUR_JPY']) if row['EUR_JPY'] else None
                processed_predrawdown.eur_krw = float(row['EUR_KRW']) if row['EUR_KRW'] else None
                processed_predrawdown.eur_mxn = float(row['EUR_MXN']) if row['EUR_MXN'] else None
                processed_predrawdown.eur_nok = float(row['EUR_NOK']) if row['EUR_NOK'] else None
                processed_predrawdown.eur_pln = float(row['EUR_PLN']) if row['EUR_PLN'] else None
                processed_predrawdown.eur_rub = float(row['EUR_RUB']) if row['EUR_RUB'] else None
                processed_predrawdown.eur_sar = float(row['EUR_SAR']) if row['EUR_SAR'] else None
                processed_predrawdown.eur_sek = float(row['EUR_SEK']) if row['EUR_SEK'] else None
                processed_predrawdown.eur_thb = float(row['EUR_THB']) if row['EUR_THB'] else None
                processed_predrawdown.eur_try = float(row['EUR_TRY']) if row['EUR_TRY'] else None
                processed_predrawdown.eur_usd = float(row['EUR_USD']) if row['EUR_USD'] else None

                processed_predrawdown.gbp_gbp = float(row['GBP_GBP']) if row['GBP_GBP'] else None
                processed_predrawdown.gbp_idr = float(row['GBP_IDR']) if row['GBP_IDR'] else None
                processed_predrawdown.gbp_ils = float(row['GBP_ILS']) if row['GBP_ILS'] else None
                processed_predrawdown.gbp_inr = float(row['GBP_INR']) if row['GBP_INR'] else None
                processed_predrawdown.gbp_jpy = float(row['GBP_JPY']) if row['GBP_JPY'] else None
                processed_predrawdown.gbp_krw = float(row['GBP_KRW']) if row['GBP_KRW'] else None
                processed_predrawdown.gbp_mxn = float(row['GBP_MXN']) if row['GBP_MXN'] else None
                processed_predrawdown.gbp_nok = float(row['GBP_NOK']) if row['GBP_NOK'] else None
                processed_predrawdown.gbp_pln = float(row['GBP_PLN']) if row['GBP_PLN'] else None
                processed_predrawdown.gbp_rub = float(row['GBP_RUB']) if row['GBP_RUB'] else None
                processed_predrawdown.gbp_sar = float(row['GBP_SAR']) if row['GBP_SAR'] else None
                processed_predrawdown.gbp_sek = float(row['GBP_SEK']) if row['GBP_SEK'] else None
                processed_predrawdown.gbp_thb = float(row['GBP_THB']) if row['GBP_THB'] else None
                processed_predrawdown.gbp_try = float(row['GBP_TRY']) if row['GBP_TRY'] else None
                processed_predrawdown.gbp_usd = float(row['GBP_USD']) if row['GBP_USD'] else None

                processed_predrawdown.idr_idr = float(row['IDR_IDR']) if row['IDR_IDR'] else None
                processed_predrawdown.idr_ils = float(row['IDR_ILS']) if row['IDR_ILS'] else None
                processed_predrawdown.idr_inr = float(row['IDR_INR']) if row['IDR_INR'] else None
                processed_predrawdown.idr_jpy = float(row['IDR_JPY']) if row['IDR_JPY'] else None
                processed_predrawdown.idr_krw = float(row['IDR_KRW']) if row['IDR_KRW'] else None
                processed_predrawdown.idr_mxn = float(row['IDR_MXN']) if row['IDR_MXN'] else None
                processed_predrawdown.idr_nok = float(row['IDR_NOK']) if row['IDR_NOK'] else None
                processed_predrawdown.idr_pln = float(row['IDR_PLN']) if row['IDR_PLN'] else None
                processed_predrawdown.idr_rub = float(row['IDR_RUB']) if row['IDR_RUB'] else None
                processed_predrawdown.idr_sar = float(row['IDR_SAR']) if row['IDR_SAR'] else None
                processed_predrawdown.idr_sek = float(row['IDR_SEK']) if row['IDR_SEK'] else None
                processed_predrawdown.idr_thb = float(row['IDR_THB']) if row['IDR_THB'] else None
                processed_predrawdown.idr_try = float(row['IDR_TRY']) if row['IDR_TRY'] else None
                processed_predrawdown.idr_usd = float(row['IDR_USD']) if row['IDR_USD'] else None

                processed_predrawdown.ils_ils = float(row['ILS_ILS']) if row['ILS_ILS'] else None
                processed_predrawdown.ils_inr = float(row['ILS_INR']) if row['ILS_INR'] else None
                processed_predrawdown.ils_jpy = float(row['ILS_JPY']) if row['ILS_JPY'] else None
                processed_predrawdown.ils_krw = float(row['ILS_KRW']) if row['ILS_KRW'] else None
                processed_predrawdown.ils_mxn = float(row['ILS_MXN']) if row['ILS_MXN'] else None
                processed_predrawdown.ils_nok = float(row['ILS_NOK']) if row['ILS_NOK'] else None
                processed_predrawdown.ils_pln = float(row['ILS_PLN']) if row['ILS_PLN'] else None
                processed_predrawdown.ils_rub = float(row['ILS_RUB']) if row['ILS_RUB'] else None
                processed_predrawdown.ils_sar = float(row['ILS_SAR']) if row['ILS_SAR'] else None
                processed_predrawdown.ils_sek = float(row['ILS_SEK']) if row['ILS_SEK'] else None
                processed_predrawdown.ils_thb = float(row['ILS_THB']) if row['ILS_THB'] else None
                processed_predrawdown.ils_try = float(row['ILS_TRY']) if row['ILS_TRY'] else None
                processed_predrawdown.ils_usd = float(row['ILS_USD']) if row['ILS_USD'] else None

                processed_predrawdown.inr_inr = float(row['INR_INR']) if row['INR_INR'] else None
                processed_predrawdown.inr_jpy = float(row['INR_JPY']) if row['INR_JPY'] else None
                processed_predrawdown.inr_krw = float(row['INR_KRW']) if row['INR_KRW'] else None
                processed_predrawdown.inr_mxn = float(row['INR_MXN']) if row['INR_MXN'] else None
                processed_predrawdown.inr_nok = float(row['INR_NOK']) if row['INR_NOK'] else None
                processed_predrawdown.inr_pln = float(row['INR_PLN']) if row['INR_PLN'] else None
                processed_predrawdown.inr_rub = float(row['INR_RUB']) if row['INR_RUB'] else None
                processed_predrawdown.inr_sar = float(row['INR_SAR']) if row['INR_SAR'] else None
                processed_predrawdown.inr_sek = float(row['INR_SEK']) if row['INR_SEK'] else None
                processed_predrawdown.inr_thb = float(row['INR_THB']) if row['INR_THB'] else None
                processed_predrawdown.inr_try = float(row['INR_TRY']) if row['INR_TRY'] else None
                processed_predrawdown.inr_usd = float(row['INR_USD']) if row['INR_USD'] else None

                processed_predrawdown.jpy_jpy = float(row['JPY_JPY']) if row['JPY_JPY'] else None
                processed_predrawdown.jpy_krw = float(row['JPY_KRW']) if row['JPY_KRW'] else None
                processed_predrawdown.jpy_mxn = float(row['JPY_MXN']) if row['JPY_MXN'] else None
                processed_predrawdown.jpy_nok = float(row['JPY_NOK']) if row['JPY_NOK'] else None
                processed_predrawdown.jpy_pln = float(row['JPY_PLN']) if row['JPY_PLN'] else None
                processed_predrawdown.jpy_rub = float(row['JPY_RUB']) if row['JPY_RUB'] else None
                processed_predrawdown.jpy_sar = float(row['JPY_SAR']) if row['JPY_SAR'] else None
                processed_predrawdown.jpy_sek = float(row['JPY_SEK']) if row['JPY_SEK'] else None
                processed_predrawdown.jpy_thb = float(row['JPY_THB']) if row['JPY_THB'] else None
                processed_predrawdown.jpy_try = float(row['JPY_TRY']) if row['JPY_TRY'] else None
                processed_predrawdown.jpy_usd = float(row['JPY_USD']) if row['JPY_USD'] else None

                processed_predrawdown.krw_krw = float(row['KRW_KRW']) if row['KRW_KRW'] else None
                processed_predrawdown.krw_mxn = float(row['KRW_MXN']) if row['KRW_MXN'] else None
                processed_predrawdown.krw_nok = float(row['KRW_NOK']) if row['KRW_NOK'] else None
                processed_predrawdown.krw_pln = float(row['KRW_PLN']) if row['KRW_PLN'] else None
                processed_predrawdown.krw_rub = float(row['KRW_RUB']) if row['KRW_RUB'] else None
                processed_predrawdown.krw_sar = float(row['KRW_SAR']) if row['KRW_SAR'] else None
                processed_predrawdown.krw_sek = float(row['KRW_SEK']) if row['KRW_SEK'] else None
                processed_predrawdown.krw_thb = float(row['KRW_THB']) if row['KRW_THB'] else None
                processed_predrawdown.krw_try = float(row['KRW_TRY']) if row['KRW_TRY'] else None
                processed_predrawdown.krw_usd = float(row['KRW_USD']) if row['KRW_USD'] else None

                processed_predrawdown.mxn_mxn = float(row['MXN_MXN']) if row['MXN_MXN'] else None
                processed_predrawdown.mxn_nok = float(row['MXN_NOK']) if row['MXN_NOK'] else None
                processed_predrawdown.mxn_pln = float(row['MXN_PLN']) if row['MXN_PLN'] else None
                processed_predrawdown.mxn_rub = float(row['MXN_RUB']) if row['MXN_RUB'] else None
                processed_predrawdown.mxn_sar = float(row['MXN_SAR']) if row['MXN_SAR'] else None
                processed_predrawdown.mxn_sek = float(row['MXN_SEK']) if row['MXN_SEK'] else None
                processed_predrawdown.mxn_thb = float(row['MXN_THB']) if row['MXN_THB'] else None
                processed_predrawdown.mxn_try = float(row['MXN_TRY']) if row['MXN_TRY'] else None
                processed_predrawdown.mxn_usd = float(row['MXN_USD']) if row['MXN_USD'] else None

                processed_predrawdown.nok_nok = float(row['NOK_NOK']) if row['NOK_NOK'] else None
                processed_predrawdown.nok_pln = float(row['NOK_PLN']) if row['NOK_PLN'] else None
                processed_predrawdown.nok_rub = float(row['NOK_RUB']) if row['NOK_RUB'] else None
                processed_predrawdown.nok_sar = float(row['NOK_SAR']) if row['NOK_SAR'] else None
                processed_predrawdown.nok_sek = float(row['NOK_SEK']) if row['NOK_SEK'] else None
                processed_predrawdown.nok_thb = float(row['NOK_THB']) if row['NOK_THB'] else None
                processed_predrawdown.nok_try = float(row['NOK_TRY']) if row['NOK_TRY'] else None
                processed_predrawdown.nok_usd = float(row['NOK_USD']) if row['NOK_USD'] else None

                processed_predrawdown.pln_pln = float(row['PLN_PLN']) if row['PLN_PLN'] else None
                processed_predrawdown.pln_rub = float(row['PLN_RUB']) if row['PLN_RUB'] else None
                processed_predrawdown.pln_sar = float(row['PLN_SAR']) if row['PLN_SAR'] else None
                processed_predrawdown.pln_sek = float(row['PLN_SEK']) if row['PLN_SEK'] else None
                processed_predrawdown.pln_thb = float(row['PLN_THB']) if row['PLN_THB'] else None
                processed_predrawdown.pln_try = float(row['PLN_TRY']) if row['PLN_TRY'] else None
                processed_predrawdown.pln_usd = float(row['PLN_USD']) if row['PLN_USD'] else None

                processed_predrawdown.rub_rub = float(row['RUB_RUB']) if row['RUB_RUB'] else None
                processed_predrawdown.rub_sar = float(row['RUB_SAR']) if row['RUB_SAR'] else None
                processed_predrawdown.rub_sek = float(row['RUB_SEK']) if row['RUB_SEK'] else None
                processed_predrawdown.rub_thb = float(row['RUB_THB']) if row['RUB_THB'] else None
                processed_predrawdown.rub_try = float(row['RUB_TRY']) if row['RUB_TRY'] else None
                processed_predrawdown.rub_usd = float(row['RUB_USD']) if row['RUB_USD'] else None

                processed_predrawdown.sar_sar = float(row['SAR_SAR']) if row['SAR_SAR'] else None
                processed_predrawdown.sar_sek = float(row['SAR_SEK']) if row['SAR_SEK'] else None
                processed_predrawdown.sar_thb = float(row['SAR_THB']) if row['SAR_THB'] else None
                processed_predrawdown.sar_try = float(row['SAR_TRY']) if row['SAR_TRY'] else None
                processed_predrawdown.sar_usd = float(row['SAR_USD']) if row['SAR_USD'] else None

                processed_predrawdown.sek_sek = float(row['SEK_SEK']) if row['SEK_SEK'] else None
                processed_predrawdown.sek_thb = float(row['SEK_THB']) if row['SEK_THB'] else None
                processed_predrawdown.sek_try = float(row['SEK_TRY']) if row['SEK_TRY'] else None
                processed_predrawdown.sek_usd = float(row['SEK_USD']) if row['SEK_USD'] else None

                processed_predrawdown.thb_thb = float(row['THB_THB']) if row['THB_THB'] else None
                processed_predrawdown.thb_try = float(row['THB_TRY']) if row['THB_TRY'] else None
                processed_predrawdown.thb_usd = float(row['THB_USD']) if row['THB_USD'] else None

                processed_predrawdown.try_try = float(row['TRY_TRY']) if row['TRY_TRY'] else None
                processed_predrawdown.try_usd = float(row['TRY_USD']) if row['TRY_USD'] else None

                processed_predrawdown.usd_usd = float(row['USD_USD']) if row['USD_USD'] else None

                # 保存到数据库
                processed_predrawdown.save()

        self.stdout.write(self.style.SUCCESS('Successfully imported data from CSV file'))