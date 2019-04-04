import os
import shutil
from stat import S_IRWXU, S_IRGRP, S_IXGRP, S_IROTH, S_IXOTH, filemode

from podder_task_base.task_initializer.builders import MkdirBuilder
from podder_task_base.task_initializer import templates


class TestMkdirBuilder:
    TARGET_DIR = "tests/tmp"
    CHMOD755 = S_IRWXU | S_IRGRP | S_IXGRP | S_IROTH | S_IXOTH

    def setup_method(self, _method):
        if not os.path.exists(self.TARGET_DIR):
            os.mkdir(self.TARGET_DIR)

    def teardown_method(self, _method):
        if os.path.exists(self.TARGET_DIR):
            shutil.rmtree(self.TARGET_DIR)

    def test_mkdir_builder_execute_option_none(self):
        templates_dir = os.path.dirname(templates.__file__)
        file = "__init__.py"
        option = None
        MkdirBuilder(templates_dir).execute(self.TARGET_DIR, file, option)
        assert os.path.isdir(os.path.join(self.TARGET_DIR, file))

    def test_mkdir_builder_execute_option_755(self):
        templates_dir = os.path.dirname(templates.__file__)
        file = "__init__.py"
        option = self.CHMOD755
        MkdirBuilder(templates_dir).execute(self.TARGET_DIR, file, option)

        dst_path = os.path.join(self.TARGET_DIR, file)
        assert os.path.isdir(dst_path)

        statinfo = os.stat(dst_path)
        mode = statinfo.st_mode
        assert filemode(mode) == 'drwxr-xr-x'