"""31. Print values of all below
	round_num = 15.456
	final_val = round(round_num, 2)
	val1=decimal.Decimal(round_num).quantize(decimal.Decimal('0.00'), rounding=decimal.ROUND_CEILING)
	val1=decimal.Decimal(round_num).quantize(decimal.Decimal('0.00'), rounding=decimal.ROUND_DOWN)
	val1=decimal.Decimal(round_num).quantize(decimal.Decimal('0.00'), rounding=decimal.ROUND_FLOOR)
	val1=decimal.Decimal(round_num).quantize(decimal.Decimal('0.00'), rounding=decimal.ROUND_HALF_DOWN)
	val1=decimal.Decimal(round_num).quantize(decimal.Decimal('0.00'), rounding=decimal.ROUND_HALF_EVEN)
	val1=decimal.Decimal(round_num).quantize(decimal.Decimal('0.00'), rounding=decimal.ROUND_HALF_UP)
	val1=decimal.Decimal(round_num).quantize(decimal.Decimal('0.00'), rounding=decimal.ROUND_UP)"""
import decimal
import logging
logger=logging.getLogger()
fhandler=logging.FileHandler(filename='6test.log', mode='a')
formatter=logging.Formatter('%(asctime)s - %(message)s', datefmt='%d-%b-%y %H:%M:%S')
fhandler.setFormatter(formatter)
logger.addHandler(fhandler)
logger.setLevel(logging.INFO)
round_num = 15.456
final_val = round(round_num, 2)
val1=decimal.Decimal(round_num).quantize(decimal.Decimal('0.00'), rounding=decimal.ROUND_CEILING)
logging.debug(val1)
val1=decimal.Decimal(round_num).quantize(decimal.Decimal('0.00'), rounding=decimal.ROUND_DOWN)
logging.debug(val1)
val1=decimal.Decimal(round_num).quantize(decimal.Decimal('0.00'), rounding=decimal.ROUND_FLOOR)
logging.debug(val1)
val1=decimal.Decimal(round_num).quantize(decimal.Decimal('0.00'), rounding=decimal.ROUND_HALF_DOWN)
logging.debug(val1)
val1=decimal.Decimal(round_num).quantize(decimal.Decimal('0.00'), rounding=decimal.ROUND_HALF_EVEN)
logging.debug(val1)
val1=decimal.Decimal(round_num).quantize(decimal.Decimal('0.00'), rounding=decimal.ROUND_HALF_UP)
logging.debug(val1)
val1=decimal.Decimal(round_num).quantize(decimal.Decimal('0.00'), rounding=decimal.ROUND_UP)
logging.debug(val1)

"""Output
15.46
15.45
15.45
15.46
15.46
15.46
15.46"""