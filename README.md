# E-commerce_Bendy

# sudo apt install python3.8-venv
    python3 -m venv env
    source env/bin/activate
# installation de django
    pip install django
# création de projet dans Django
    django-admin startproject shop .
# création de l'application dans django
    python3 manage.py startapp store
# execution de l'application en local
    python3 manage.py runserver

# commandes de migration de ma base de données
    python manage.py makemigrations
    python manage.py migrate
# creation de user dans la page admin
    python3 manage.py createsuperuser

user = request.user
    product = product
    cart, _ = Cart.objects.get_or_create(user=user)
    order, created = Order.objects.get_or_create(user=user, product=product) 

    if created:
        cart.orders.add(order)
        cart.save()
    else:
        order.quantity += 1
        order.save()
    return redirect(reverse("product", kwargs={"slug": slug}))