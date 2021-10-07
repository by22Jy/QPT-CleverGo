# -*- coding: utf-8 -*-
# @Time    : 2021/10/7 10:56
# @Author  : He Ruizhi
# @File    : ctbase.py
# @Software: PyCharm

import pygame


class CtBase:
    """pygame控件基类，所有自定义控件均需继承CtBase"""

    def update(self, event: pygame.event) -> ...:
        """
        根据pygame.event对控件状态进行更新

        所有控件类均需重写该方法
        """
        raise NotImplementedError
