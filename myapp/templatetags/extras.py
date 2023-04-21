from django import template
register = template.Library() #登記 模板圖書館

#製作標籤過濾器
@register.filter
def extras(List, i):
    return List[int(i)]