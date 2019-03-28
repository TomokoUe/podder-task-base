import os
import shutil
from unittest.mock import patch

from podder_task_base.task_initializer.builder import Builder


class TestBuilder:
    TEST_TMP_PATH = './tests/tmp_test_builder'
    TASK_NAME = 'test-sample-task'

    def teardown_method(self, _method):
        if os.path.exists(self.TEST_TMP_PATH):
            shutil.rmtree(self.TEST_TMP_PATH)


    def test_builder(self):
        Builder(self.TASK_NAME, self.TEST_TMP_PATH).init_task()

        this_dir = os.path.dirname(os.path.abspath(__file__))
        templates_dir = os.path.join(this_dir, "../../podder_task_base/task_initializer/templates")

        base_set = set()
        for file in self._find_all_files(templates_dir):
            path = os.path.relpath(file, start=templates_dir)
            base_set.add(path)

        test_set = set()
        for file in self._find_all_files(self.TEST_TMP_PATH):
            path = os.path.relpath(file, start=self.TEST_TMP_PATH)
            test_set.add(path)

        print("--base_set--")
        for path in sorted(base_set):
            print(path)
        print("--test_set--")
        for path in sorted(test_set):
            print(path)

        assert base_set == test_set

    def _find_all_files(self, directory):
        for root, dirs, files in os.walk(directory):
            for file in files:
                yield os.path.join(root, file)
