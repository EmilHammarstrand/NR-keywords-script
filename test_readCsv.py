import readCsv
import pytest


class TestReadCsv:

    def test_add_key_words_verify_replace_keywords(self):
        document = {'id': '475dec69-10c9-4bc6-8312-3caa266fb028', 'name': 'PHP', 'description': 'This is an observability pack for PHP applications.\nThis pack relies on the New Relic PHP agent, with distributed tracing enabled (https://docs.newrelic.com/docs/agents/php-agent/features/distributed-tracing-php-agent/)\n\n', 'level': 'New Relic', 'logo': 'logo.jpg', 'website': 'https://www.php.net/', 'authors': ['New Relic', 'Stijn Polfliet'], 'documentation': [{'name': 'PHP', 'description': 'PHP is a general-purpose scripting language especially suited to web development.', 'url': 'https://docs.newrelic.com/docs/agents/php-agent/getting-started/php-agent-compatibility-requirements/'}], 'instrumentation': [{'type': 'newrelic-apm', 'name': 'php'}], 'keywords': ['apm', 'php', 'language agent']}

        # Before replacing keywords, verify original values
        assert document['keywords'] == ['apm', 'php', 'language agent']

        pack_keywords = 'apm, nisse'
        result = readCsv.add_key_words(document, pack_keywords)

        # Verify that replacement of keywords works
        assert result['keywords'] == ['apm', 'nisse']

    def test_add_key_words_verify_add_keywords_if_not_exist_in_original(self):
        document = {'id': '475dec69-10c9-4bc6-8312-3caa266fb028', 'name': 'PHP', 'description': 'This is an observability pack for PHP applications.\nThis pack relies on the New Relic PHP agent, with distributed tracing enabled (https://docs.newrelic.com/docs/agents/php-agent/features/distributed-tracing-php-agent/)\n\n', 'level': 'New Relic', 'logo': 'logo.jpg', 'website': 'https://www.php.net/', 'authors': ['New Relic', 'Stijn Polfliet'], 'documentation': [{'name': 'PHP', 'description': 'PHP is a general-purpose scripting language especially suited to web development.', 'url': 'https://docs.newrelic.com/docs/agents/php-agent/getting-started/php-agent-compatibility-requirements/'}], 'instrumentation': [{'type': 'newrelic-apm', 'name': 'php'}]}

        # Verify that no keywords exists in document
        with pytest.raises(KeyError):
            assert document['keywords'] == 'Nothing should be here'

        pack_keywords = 'apm, nisse'
        result = readCsv.add_key_words(document, pack_keywords)

        # Verify that adding keywords works
        assert result['keywords'] == ['apm', 'nisse']

    def test_add_key_words_verify_do_not_add_keywords_field_if_keywords_not_exists(self):
        document = {'id': '475dec69-10c9-4bc6-8312-3caa266fb028', 'name': 'PHP', 'description': 'This is an observability pack for PHP applications.\nThis pack relies on the New Relic PHP agent, with distributed tracing enabled (https://docs.newrelic.com/docs/agents/php-agent/features/distributed-tracing-php-agent/)\n\n', 'level': 'New Relic', 'logo': 'logo.jpg', 'website': 'https://www.php.net/', 'authors': ['New Relic', 'Stijn Polfliet'], 'documentation': [{'name': 'PHP', 'description': 'PHP is a general-purpose scripting language especially suited to web development.', 'url': 'https://docs.newrelic.com/docs/agents/php-agent/getting-started/php-agent-compatibility-requirements/'}], 'instrumentation': [{'type': 'newrelic-apm', 'name': 'php'}]}

        pack_keywords = None
        result = readCsv.add_key_words(document, pack_keywords)

        # Verify that we do not add keyword field, when no keywords defined in our definition "file"
        with pytest.raises(KeyError):
            assert result['keywords'] == 'Nothing should be here'