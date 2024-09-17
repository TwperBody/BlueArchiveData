from pkg.plugin.models import *
from pkg.plugin.context import register,handler,BasePlugin,APIHost,EventContext

import requests
import json

def get_boss_info(server):
    api_url = 'https://api.arona.icu/raids/boss/info'
    file_path = 'plugins/BlueArchiveData/token.json'
    try:
        # 打开文件并读取内容
        with open(file_path, 'r', encoding='utf-8') as file:
            data = json.load(file)

        # 检查tokens数组是否不为空，并提取token
        if 'tokens' in data and len(data['tokens']) > 0:
            token = data['tokens'][0]['token']
        else:
            return "没有找到token"

        # 请求的参数
        payload = {
            'server': server
        }

        # 设置认证头部
        headers = {
            'Authorization': token,
            'Content-Type': 'application/json'
        }

        # 发送POST请求
        response = requests.post(api_url, json=payload, headers=headers)

        # 检查请求是否成功并且数据有效
        if response.status_code == 200 and response.json().get('code') == 200:
            # 解析返回的JSON数据
            data = response.json().get('data', [])
            
            # 格式化Boss信息
            formatted_info = []
            for boss in data:
                if boss:  # 确保boss信息不为空
                    formatted_info.append(f"Boss名称: {boss.get('Name', '未知')}")
                    formatted_info.append(f"路径名: {boss.get('PathName', '无路径名')}")
                    formatted_info.append(f"组名: {boss.get('GroupName', '无组名')}")
                    formatted_info.append(f"简介: {boss.get('Profile', '无简介')}")
                    formatted_info.append("-" * 30)  # 分隔线
            return "\n".join(formatted_info)
        else:
            return "请求失败或数据无效"
    except Exception as e:
        return f"发生错误: {e}"

# 注册插件
@register(name="BlueArchiveData", description="蔚蓝档案数据库", version="0.1", author="TwperBody")
class KeywordActiveReviewPlugin(BasePlugin):

    # 插件加载时触发
    def __init__(self, host: APIHost):
        pass

    async def initialize(self):
        pass

    # 当收到user消息时触发
    @handler(PersonNormalMessageReceived)
    async def PersonNormalMessageReceived(self, ctx: EventContext):
        
        msg = ctx.event.text_message  # 这里的 event 即为 PersonNormalMessageReceived 的对象
        if msg == "帮助" :
            self.ap.logger.debug("{} \n boss列表 <服务器>".format(ctx.event.sender_id))
            ctx.add_return("reply", ["{} \n boss列表 <服务器>".format(ctx.event.sender_id)])
            # 阻止该事件默认行为（向接口获取回复）
            ctx.prevent_default()
        elif msg == "boss列表 官服":
            self.ap.logger.debug(get_boss_info(1).format(ctx.event.sender_id))
            ctx.add_return("reply", [ get_boss_info(1).format(ctx.event.sender_id)])
            ctx.add_return("reply", ["数据来源于 a r o n a . i c u ".format(ctx.event.sender_id)])
            # 阻止该事件默认行为（向接口获取回复）
            ctx.prevent_default()
        elif msg == "boss列表 B服":
            self.ap.logger.debug(get_boss_info(2).format(ctx.event.sender_id))
            ctx.add_return("reply", [ get_boss_info(2).format(ctx.event.sender_id)])
            ctx.add_return("reply", ["数据来源于 a r o n a . i c u ".format(ctx.event.sender_id)])
            # 阻止该事件默认行为（向接口获取回复）
            ctx.prevent_default()
        elif msg == "boss列表 日服":
            self.ap.logger.debug(get_boss_info(3).format(ctx.event.sender_id))
            ctx.add_return("reply", [ get_boss_info(3).format(ctx.event.sender_id)])
            ctx.add_return("reply", ["数据来源于 a r o n a . i c u ".format(ctx.event.sender_id)])
            # 阻止该事件默认行为（向接口获取回复）
            ctx.prevent_default()
        elif msg == "boss列表 综合":
            self.ap.logger.debug(get_boss_info(4).format(ctx.event.sender_id))
            ctx.add_return("reply", [ get_boss_info(4).format(ctx.event.sender_id)])
            ctx.add_return("reply", ["数据来源于 a r o n a . i c u ".format(ctx.event.sender_id)])
            # 阻止该事件默认行为（向接口获取回复）
            ctx.prevent_default()
        elif msg == "boss列表 全球":
            self.ap.logger.debug(get_boss_info(5).format(ctx.event.sender_id))
            ctx.add_return("reply", [ get_boss_info(5).format(ctx.event.sender_id)])
            ctx.add_return("reply", ["数据来源于 a r o n a . i c u ".format(ctx.event.sender_id)])
            # 阻止该事件默认行为（向接口获取回复）
            ctx.prevent_default()
        elif msg == "boss列表 港澳台":
            self.ap.logger.debug(get_boss_info(6).format(ctx.event.sender_id))
            ctx.add_return("reply", [ get_boss_info(6).format(ctx.event.sender_id)])
            ctx.add_return("reply", ["数据来源于 a r o n a . i c u ".format(ctx.event.sender_id)])
            # 阻止该事件默认行为（向接口获取回复）
            ctx.prevent_default()
        elif msg == "boss列表 韩服":
            self.ap.logger.debug(get_boss_info(7).format(ctx.event.sender_id))
            ctx.add_return("reply", [ get_boss_info(7).format(ctx.event.sender_id)])
            ctx.add_return("reply", ["数据来源于 a r o n a . i c u ".format(ctx.event.sender_id)])
            # 阻止该事件默认行为（向接口获取回复）
            ctx.prevent_default()
        elif msg == "boss列表 亚服":
            self.ap.logger.debug(get_boss_info(8).format(ctx.event.sender_id))
            ctx.add_return("reply", [ get_boss_info(8).format(ctx.event.sender_id)])
            ctx.add_return("reply", ["数据来源于 a r o n a . i c u ".format(ctx.event.sender_id)])
            # 阻止该事件默认行为（向接口获取回复）
            ctx.prevent_default()
        elif msg == "boss列表 北美服":
            self.ap.logger.debug(get_boss_info(9).format(ctx.event.sender_id))
            ctx.add_return("reply", [ get_boss_info(9).format(ctx.event.sender_id)])
            ctx.add_return("reply", ["数据来源于 a r o n a . i c u ".format(ctx.event.sender_id)])
            # 阻止该事件默认行为（向接口获取回复）
            ctx.prevent_default()
        


    # 当收到群消息时触发
    @handler(GroupNormalMessageReceived)
    async def group_normal_message_received(self, ctx: EventContext):
        msg = ctx.event.text_message  # 这里的 event 即为 PersonNormalMessageReceived 的对象
        if msg == "帮助" :
            self.ap.logger.debug("{} \n boss列表 <服务器>".format(ctx.event.sender_id))
            ctx.add_return("reply", ["{} \n boss列表 <服务器>".format(ctx.event.sender_id)])
            # 阻止该事件默认行为（向接口获取回复）
            ctx.prevent_default()
        elif msg == "boss列表 官服":
            self.ap.logger.debug(get_boss_info(1).format(ctx.event.sender_id))
            ctx.add_return("reply", [ get_boss_info(1).format(ctx.event.sender_id)])
            ctx.add_return("reply", ["数据来源于 a r o n a . i c u ".format(ctx.event.sender_id)])
            # 阻止该事件默认行为（向接口获取回复）
            ctx.prevent_default()
        elif msg == "boss列表 B服":
            self.ap.logger.debug(get_boss_info(2).format(ctx.event.sender_id))
            ctx.add_return("reply", [ get_boss_info(2).format(ctx.event.sender_id)])
            ctx.add_return("reply", ["数据来源于 a r o n a . i c u ".format(ctx.event.sender_id)])
            # 阻止该事件默认行为（向接口获取回复）
            ctx.prevent_default()
        elif msg == "boss列表 日服":
            self.ap.logger.debug(get_boss_info(3).format(ctx.event.sender_id))
            ctx.add_return("reply", [ get_boss_info(3).format(ctx.event.sender_id)])
            ctx.add_return("reply", ["数据来源于 a r o n a . i c u ".format(ctx.event.sender_id)])
            # 阻止该事件默认行为（向接口获取回复）
            ctx.prevent_default()
        elif msg == "boss列表 综合":
            self.ap.logger.debug(get_boss_info(4).format(ctx.event.sender_id))
            ctx.add_return("reply", [ get_boss_info(4).format(ctx.event.sender_id)])
            ctx.add_return("reply", ["数据来源于 a r o n a . i c u ".format(ctx.event.sender_id)])
            # 阻止该事件默认行为（向接口获取回复）
            ctx.prevent_default()
        elif msg == "boss列表 全球":
            self.ap.logger.debug(get_boss_info(5).format(ctx.event.sender_id))
            ctx.add_return("reply", [ get_boss_info(5).format(ctx.event.sender_id)])
            ctx.add_return("reply", ["数据来源于 a r o n a . i c u ".format(ctx.event.sender_id)])
            # 阻止该事件默认行为（向接口获取回复）
            ctx.prevent_default()
        elif msg == "boss列表 港澳台":
            self.ap.logger.debug(get_boss_info(6).format(ctx.event.sender_id))
            ctx.add_return("reply", [ get_boss_info(6).format(ctx.event.sender_id)])
            ctx.add_return("reply", ["数据来源于 a r o n a . i c u ".format(ctx.event.sender_id)])
            # 阻止该事件默认行为（向接口获取回复）
            ctx.prevent_default()
        elif msg == "boss列表 韩服":
            self.ap.logger.debug(get_boss_info(7).format(ctx.event.sender_id))
            ctx.add_return("reply", [ get_boss_info(7).format(ctx.event.sender_id)])
            ctx.add_return("reply", ["数据来源于 a r o n a . i c u ".format(ctx.event.sender_id)])
            # 阻止该事件默认行为（向接口获取回复）
            ctx.prevent_default()
        elif msg == "boss列表 亚服":
            self.ap.logger.debug(get_boss_info(8).format(ctx.event.sender_id))
            ctx.add_return("reply", [ get_boss_info(8).format(ctx.event.sender_id)])
            ctx.add_return("reply", ["数据来源于 a r o n a . i c u ".format(ctx.event.sender_id)])
            # 阻止该事件默认行为（向接口获取回复）
            ctx.prevent_default()
        elif msg == "boss列表 北美服":
            self.ap.logger.debug(get_boss_info(9).format(ctx.event.sender_id))
            ctx.add_return("reply", [ get_boss_info(9).format(ctx.event.sender_id)])
            ctx.add_return("reply", ["数据来源于 a r o n a . i c u ".format(ctx.event.sender_id)])
            # 阻止该事件默认行为（向接口获取回复）
            ctx.prevent_default()

    def __del__(self):
        pass
