from typing import Any, Text, Dict, List
from rasa_sdk import Action, Tracker
from rasa_sdk.executor import CollectingDispatcher
from gql import Client, gql
from gql.transport.requests import RequestsHTTPTransport

class QueryNeo4jSuppliers(Action):
    def name(self) -> Text:
        return "action_query_neo4j_suppliers"

    def run(self, dispatcher: CollectingDispatcher, tracker: Tracker, domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        query = gql('''
          query Suppliers {
              suppliers {
                  location
                  material
                  name
                  supplierID
              }
          }
        ''')

        transport = RequestsHTTPTransport(
            url='http://localhost:4000/graphql',
            use_json=True,
        )

        client = Client(transport=transport, fetch_schema_from_transport=True)

        try:
            result = client.execute(query)
            suppliers = result.get('suppliers', [])
            suppliers_list = "\n".join([f"- {supplier['supplierID']}, {supplier['name']}, {supplier['location']}, Material: {supplier['material']}" for supplier in suppliers])
            dispatcher.utter_message(text=f"Here are the list of suppliers:\n{suppliers_list}")
        except Exception as e:
            dispatcher.utter_message(text="Failed to query suppliers from Neo4j.")
            print(e)

        return []


class QueryNeo4jProducts(Action):
    def name(self) -> Text:
        return "action_query_neo4j_products"

    def run(self, dispatcher: CollectingDispatcher, tracker: Tracker, domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        query = gql('''
          query Products {
              products {
                  category
                  manufacturingCost
                  name
                  productID
              }
          }
        ''')

        transport = RequestsHTTPTransport(
            url='http://localhost:4000/graphql',
            use_json=True,
        )

        client = Client(transport=transport, fetch_schema_from_transport=True)

        try:
            result = client.execute(query)
            products = result.get('products', [])
            product_list = "\n".join([f"- {product['productID']}, {product['name']}, Category: {product['category']}, Manufacturing Cost: {product['manufacturingCost']}" for product in products])
            dispatcher.utter_message(text=f"Here are the list of products:\n{product_list}")
        except Exception as e:
            dispatcher.utter_message(text="Failed to query products from Neo4j.")
            print(e)

        return []

class QueryNeo4jManufacturers(Action):
    def name(self) -> Text:
        return "action_query_neo4j_manufacturers"

    def run(self, dispatcher: CollectingDispatcher, tracker: Tracker, domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        query = gql('''
          query Manufacturers {
              manufacturers {
                  location
                  manufacturerID
                  name
                  product
              }
          }
        ''')

        transport = RequestsHTTPTransport(
            url='http://localhost:4000/graphql',
            use_json=True,
        )

        client = Client(transport=transport, fetch_schema_from_transport=True)

        try:
            result = client.execute(query)
            manufacturers = result.get('manufacturers', [])
            manufacturer_list = "\n".join([f"- {manufacturer['manufacturerID']}, {manufacturer['name']}, {manufacturer['location']}, Product: {manufacturer['product']}" for manufacturer in manufacturers])
            dispatcher.utter_message(text=f"Here are the list of manufacturers:\n{manufacturer_list}")
        except Exception as e:
            dispatcher.utter_message(text="Failed to query manufacturers from Neo4j.")
            print(e)

        return []

class QueryNeo4jDistributors(Action):
    def name(self) -> Text:
        return "action_query_neo4j_distributors"

    def run(self, dispatcher: CollectingDispatcher, tracker: Tracker, domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        query = gql('''
          query Distributors {
              distributors {
                  distributorID
                  location
                  name
              }
          }
        ''')

        transport = RequestsHTTPTransport(
            url='http://localhost:4000/graphql',
            use_json=True,
        )

        client = Client(transport=transport, fetch_schema_from_transport=True)

        try:
            result = client.execute(query)
            distributors = result.get('distributors', [])
            distributor_list = "\n".join([f"- {distributor['distributorID']}, {distributor['name']}, {distributor['location']}" for distributor in distributors])
            dispatcher.utter_message(text=f"Here are the list of distributors:\n{distributor_list}")
        except Exception as e:
            dispatcher.utter_message(text="Failed to query distributors from Neo4j.")
            print(e)

        return []
