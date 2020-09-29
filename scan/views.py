from django.shortcuts import render
from pymongo import MongoClient


def index(request):
    if not request.method == 'POST':
        return render(request, 'index.html')
    else:
        client = MongoClient(
            'mongodb+srv://abhip1912:abcd1234@cluster0.ywymp.mongodb.net/<dbname>?retryWrites=true&w=majority')
        db = client.get_database('barcode')
        orders = db.orders
        users = db.users

        if 'orderid' in request.POST:
            print(request.POST['orderid'])
            if not request.POST['orderid']:
                data = list(orders.find())
            else:
                data = list(orders.find({'orderId': request.POST['orderid']}))
            return render(request, 'home.html', {'data': data})

        else:
            mail = request.POST['email']
            pw = request.POST['pass']

            resp = list(users.find({'email': mail}))

            if len(resp) > 0:
                if resp[0]['pass'] == pw:
                    data = list(orders.find())
                    return render(request, 'home.html', {'data': data})
                else:
                    return render(request, 'index.html')
            else:
                return render(request, 'index.html')
