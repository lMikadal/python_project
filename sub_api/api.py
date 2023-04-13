from ninja import Router
from sub_api.schemas import testSchema

router = Router()

@router.get('/test')
def test(request):
    return "test api Hello World!!"

@router.get('/test1/{int:num}')
def test1(request, num: int):
    return f"test num + 1 = {num + 1}"

@router.get('/testS', response=list[testSchema])
def testS(request):
    data = [
        testSchema(name="panupong", age=23),
        testSchema(name="mikada", age=32)
	]
    return data