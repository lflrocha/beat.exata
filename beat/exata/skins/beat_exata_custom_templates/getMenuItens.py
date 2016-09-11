## Script (Python) "getMenuItens"
##bind container=container
##bind context=context
##bind namespace=
##bind script=script
##bind subpath=traverse_subpath
##parameters=
##title=


vet = []

folders = context.getFolderContents(contentFilter={'portal_type':'Folder','review_state':'published'})
for folder in folders:
    dic = {}
    sub = []
    dic['id'] = folder.id
    dic['url'] = folder.getURL()
    dic['title'] = folder.Title
    subfolders = folder.getObject().getFolderContents(contentFilter={'portal_type':'Folder','review_state':'published'})
    for subfolder in subfolders:
        subdic = {}
        subdic['id'] = subfolder.id
        subdic['url'] = subfolder.getURL()
        subdic['title'] = subfolder.Title
        sub.append(subdic)
    dic['sub'] = sub
    vet.append(dic)


return vet