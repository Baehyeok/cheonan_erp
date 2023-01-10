import uuid
from django.db import models



# Create your models here.
# class purchase_data(models.Model):
#     purchase_id = models.AutoField()



# 거래처 테이블
class client_info(models.Model):
    client_id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False, unique=True)
    client_corp_name = models.CharField(max_length=100, null=True, blank=True)          # 회사 이름
    client_name = models.CharField(max_length=100, null=True, blank=True)               # 대표 이름
    client_number = models.CharField(max_length=100, null=True, blank=True)             # 등록번호(사업자 번호)
    client_address = models.CharField(max_length=100, null=True, blank=True)            # 회사 주소
    client_type = models.CharField(max_length=100, null=True, blank=True)               # 회사 업태
    client_job_type = models.CharField(max_length=100, null=True, blank=True)           # 회사 종목
    client_email = models.CharField(max_length=100, null=True, blank=True)              # 대표 메일
    client_sub_email = models.CharField(max_length=100, null=True, blank=True)          # 경리 메일
    client_tel = models.CharField(max_length=100, null=True, blank=True)                # 대표 번호
    client_sub_tel = models.CharField(max_length=100, null=True, blank=True)            # 경리 번호
    client_fax = models.CharField(max_length=100, null=True, blank=True)                # 회사 팩스
    etc = models.CharField(max_length=100, null=True, blank=True)                       # 비고

# 재고 테이블
class item_info(models.Model):
    # 재고 아이디
    item_id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False, unique=True)
    # 거래처 아이디
    client_id = models.ForeignKey(client_info, on_delete=models.SET_NULL, null=True, blank=True)
    # 품목
    item_name = models.CharField(max_length=100, null=True, blank=True)
    # 단가 매입에서 판단 가격 변동이 일어날 수 있기 때문
    # item_one_price = models.IntegerField(null=True, blank=True)
    # 품번
    serial_number = models.CharField(max_length=100, null=True, blank=True)
    # 규격
    item_type = models.CharField(max_length=100, null=True, blank=True)
    # 수량
    count = models.IntegerField(null=True, blank=True, default=0)
    
class car_info(models.Model):
    car_id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False, unique=True)
    car_name = models.CharField(max_length=100, null=True, blank=True)
    car_type = models.CharField(max_length=100, null=True, blank=True)
    car_number = models.CharField(max_length=100, null=True, blank=True)
    


# 매입 테이블
class buy_info(models.Model):
    buy_id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False, unique=True)
    # 거래처 정보
    client_id = models.ForeignKey(client_info, on_delete=models.SET_NULL, db_column='client_id', null=True, blank=True)
    # 재고(품목) 정보
    item_id = models.ForeignKey(item_info, on_delete=models.SET_NULL, null=True, blank=True) 
    # buy_name = models.CharField(max_length=100, null=True, blank=True)
    # 구입일
    buy_date = models.DateField(null=True, blank=True)
    # 수량
    count = models.IntegerField(null=True, blank=True)
    # 단가
    unit_price = models.IntegerField(null=True, blank=True, default=0)
    # 부가세 여부
    vat_check = models.CharField(max_length=10, null=True, blank=True, default="0")
    # 
    total_money = models.IntegerField(null=True, blank=True)

    # 결재일
    pay_date = models.DateField(null=True, blank=True)
    # 결재 여부
    pay_check = models.CharField(max_length=10, null=True, blank=True, default="0")

# 매출 테이블
class sale_info(models.Model):
    sale_id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False, unique=True)
    client_id = models.ForeignKey(client_info, on_delete=models.SET_NULL, db_column='client_id', null=True, blank=True)








