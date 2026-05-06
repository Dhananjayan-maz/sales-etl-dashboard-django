from django.db.models import Sum, Count
from django.shortcuts import render, redirect
from .models import Sales
import pandas as pd
import json


def upload_file(request):
    if request.method == "POST":
        file = request.FILES['file']
        df = pd.read_csv(file)
        #print(df)

        Sales.objects.all().delete()

        # Transform
        df.dropna(inplace=True)
        df['total_amount'] = df['price'] * df['quantity']

        # Load into DB
        for _, row in df.iterrows():
            Sales.objects.create(
                order_id=row['order_id'],
                product=row['product'],
                category=row['category'],
                price=row['price'],
                quantity=row['quantity'],
                date=row['date'],
                total_amount=row['total_amount']
            )
        return redirect('dashboard')

    return render(request, "upload.html")

def dashboard(request):
    sales = Sales.objects.all()

    # KPI Metrics
    total_revenue = sales.aggregate(Sum('total_amount'))['total_amount__sum'] or 0
    total_orders = sales.aggregate(Count('id'))['id__count'] or 0

    # Top Category
    top_category_data = (
        sales.values('category')
        .annotate(total=Sum('total_amount'))
        .order_by('-total')
        .first()
    )
    top_category = top_category_data['category'] if top_category_data else "N/A"

    # Monthly Sales
    monthly_data = (
        sales.values('date')
        .annotate(total=Sum('total_amount'))
        .order_by('date')
    )

    dates = [str(item['date']) for item in monthly_data]
    totals = [float(item['total']) for item in monthly_data]

    # Category-wise Sales
    category_data = (
        sales.values('category')
        .annotate(total=Sum('total_amount'))
    )

    categories = [item['category'] for item in category_data]
    category_totals = [float(item['total']) for item in category_data]

    context = {
        "total_revenue": total_revenue,
        "total_orders": total_orders,
        "top_category": top_category,
        "dates": json.dumps(dates),
        "totals": json.dumps(totals),
        "categories": json.dumps(categories),
        "category_totals": json.dumps(category_totals),
    }

    return render(request, "dashboard.html", context)