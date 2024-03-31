# Contents of test_merge_two_sorted_list
import logging
import pytest
from LinkedList.merge_two_sorted_list import ListNode as ln
from LinkedList.merge_two_sorted_list import mergeTwoLists as mtl

logging.basicConfig(format='@(asctime)s %(levelname)-8s %(message)s',
                    datefmt='%Y-%m-%d %H:%M:%S')
logger = logging.getLogger(__name__)

class TestListNode(object):
    # @pytest.fixture(scope="session", autouse=True)
    # def target_node(self):
    #     return ln     
    def test_mergeTwoLists(self):
        logger.debug('this is a test')