def pagination(result, per_page, page):
    
    per_page = int(per_page) if per_page else 10

    page = int(page) if page else 1

    initial = (page - 1) * per_page
    final = per_page * page
    
    return result[initial:final]