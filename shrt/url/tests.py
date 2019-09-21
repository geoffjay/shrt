import json

from django.test import TestCase
from django.test import Client

from shrt.url.models import Url

# Base test case class taken from:
# https://www.sam.today/blog/testing-graphql-with-graphene-django/
class GraphQLTestCase(TestCase):

    def setUp(self):
        self._client = Client()

    def query(self, query: str, op_name: str = None):
        '''
        Args:
            query (string) - GraphQL query to run
            op_name (string) - If the query is a mutation or named query, you must
                               supply the op_name.  For anon queries ("{ ... }"),
                               should be None (default).

        Returns:
            dict, response from graphql endpoint.  The response has the "data" key.
                  It will have the "error" key if any error happened.
        '''
        body = {'query': query}
        if op_name:
            body['operation_name'] = op_name

        resp = self._client.post('/graphql',
                                 json.dumps(body),
                                 content_type='application/json')
        jresp = json.loads(resp.content.decode())
        return jresp

    def assertResponseNoErrors(self, resp: dict, expected: dict):
        '''
        Assert that the resp (as retuened from query) has the data from
        expected
        '''
        self.assertNotIn('errors', resp, 'Response had errors')
        self.assertEqual(resp['data'], expected, 'Response has correct data')


class SchemaTest(GraphQLTestCase):

    def test_create_mutation_successful(self):
        resp = self.query(
            '''
            mutation CreateUrl {
                createUrl(original: "https://github.com/geoffjay/shrt") {
                    id
                    original
                    tag
                }
            }
            ''',
            op_name='createUrl'
        )
        tag = resp['data']['createUrl']['tag']
        expected = {
            'createUrl': {
                'id': 1,
                'original': 'https://github.com/geoffjay/shrt',
                'tag': tag
            }
        }
        self.assertResponseNoErrors(resp, expected)

    def test_read_query_successful(self):
        # Manually add an entity to query
        url = Url(
            original='https://github.com/geoffjay/shrt'
        )
        url.save()
        saved = Url.objects.get(id=1)
        resp = self.query(
            '''
            query ReadUrl {
                url(id: 1) {
                    original
                    tag
                }
            }
            ''',
            op_name='url'
        )
        expected = {
            'url': {
                "original": "https://github.com/geoffjay/shrt",
                "tag": saved.tag
            }
        }
        self.assertResponseNoErrors(resp, expected)

    def test_delete_mutation_successful(self):
        resp = self.query(
            '''
            mutation DeleteUrl {
                deleteUrl(id: 1) {
                    id
                }
            }
            ''',
            op_name='createUrl'
        )
        self.assertResponseNoErrors(resp, {'deleteUrl': {'id': 1}})