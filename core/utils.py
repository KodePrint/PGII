from django.utils.html import format_html

def preview_img(name, img=None):
  no_img_svg =  '''
    <picture style="width:36px; height:36px; display:flex; align-items:center; justify-content:center;">
    <svg width="800px" height="800px" viewBox="0 0 24 24" style="width:36px; height:36px;" fill="none" xmlns="http://www.w3.org/2000/svg">
      <path d="M2 12.5001L3.75159 10.9675C4.66286 10.1702 6.03628 10.2159 6.89249 11.0721L11.1822 15.3618C11.8694 16.0491 12.9512 16.1428 13.7464 15.5839L14.0446 15.3744C15.1888 14.5702 16.7369 14.6634 17.7765 15.599L21 18.5001" stroke="currentColor" stroke-width="1.5" stroke-linecap="round"/>
      <path d="M22 2.00002L16 8M16 2L21.9999 7.99998" stroke="currentColor" stroke-width="1.5" stroke-linecap="round"/>
      <path d="M22 12C22 16.714 22 19.0711 20.5355 20.5355C19.0711 22 16.714 22 12 22C7.28595 22 4.92893 22 3.46447 20.5355C2 19.0711 2 16.714 2 12C2 10.8717 2 9.87835 2.02008 9M12 2C7.28595 2 4.92893 2 3.46447 3.46447C3.03965 3.88929 2.73806 4.38921 2.52396 5" stroke="currentColor" stroke-width="1.5" stroke-linecap="round"/>
    </svg>
    <picture>
  '''
  print(name)
  print(img)

  if img:
    return format_html('''
      <picture style="width:36px; height:36px; display:flex; align-items:center; justify-content:center;">
        <img src="%s" alt="%s logo" height="36" style="border-radius: 6px; object-fit:contain;" />
      </picture>''' % (img.url, name))
  else:
    return format_html(no_img_svg)