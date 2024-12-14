from flask import Blueprint, render_template, request
import requests

product_bp = Blueprint('product_bp', __name__)

# Base URL da API do Mercado Livre
MERCADO_LIVRE_API_BASE = "https://api.mercadolibre.com"

@product_bp.route('/')
def index():
    limit = 12
    page = int(request.args.get('page', 0))
    offset = page * limit
    query = request.args.get('q', 'informática')  # Termo de busca padrão: informática

    # Fazer a requisição para buscar produtos com o termo de busca
    response = requests.get(f"{MERCADO_LIVRE_API_BASE}/sites/MLB/search", params={"q": query, "limit": limit, "offset": offset})

    if response.status_code == 200:
        data = response.json()

        products = [
            {
                "id": item["id"],
                "title": item["title"],
                "price": item["price"],
                "thumbnail": item["thumbnail"],
                "permalink": item["permalink"]
            }
            for item in data.get("results", [])
        ]

        total_products = data.get("paging", {}).get("total", 0)
        total_pages = (total_products // limit) + (1 if total_products % limit > 0 else 0)

        max_page_links = 5
        start_page = max(0, page - max_page_links // 2)
        end_page = min(total_pages, start_page + max_page_links)

        page_links = list(range(start_page, end_page))

        return render_template("home.html", products=products, page=page, total_pages=total_pages, page_links=page_links, query=query)
    else:
        return "Erro ao carregar produtos", response.status_code


@product_bp.route('/product/<product_id>')
def product_details(product_id):
    # Faz a requisição para obter os detalhes de um produto
    response = requests.get(f"{MERCADO_LIVRE_API_BASE}/items/{product_id}")

    if response.status_code == 200:
        product_data = response.json()

        # Preparando as informações para exibição
        product = {
            "id": product_data["id"],
            "title": product_data["title"],
            "price": product_data["price"],
            "description": product_data.get("plain_text", "Descrição não disponível"),
            "thumbnail": product_data.get("thumbnail", ""),  # Imagem de baixa resolução
            "secure_thumbnail": product_data.get("secure_thumbnail", ""),  # Imagem com melhor resolução
            "pictures": product_data.get("pictures", []),  # Lista de imagens, se disponível
            "condition": product_data["condition"],
            "sold_quantity": product_data.get("sold_quantity", 0),
            "available_quantity": product_data.get("available_quantity", 0)
        }

        return render_template("product_details.html", product=product)
    else:
        return "Erro ao carregar os detalhes do produto", response.status_code
