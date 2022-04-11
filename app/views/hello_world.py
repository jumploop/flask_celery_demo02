from . import view
from app.tasks import add_together, mul_together


@view.route('/', methods=['GET', 'POST'])
def index():
    result = add_together.delay(23, 42)
    print(f"task_id:{result}")
    result2 = mul_together.delay(2, 10)
    print(result2)
    return "add_together and mul_together is running...."
