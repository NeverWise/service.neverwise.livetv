#!/usr/bin/python
import neverwise as nw, os, re, sys, requests, xbmcgui
from contextlib import closing
from datetime import datetime


def _download_epg(addon_userdata_path):

  xmltv_url = None
  response = nw.getResponse('http://epgalfasite.dyndns.tv/kodi-epgsources')
  if response.isSucceeded:
    sources_list = response.body.splitlines()
    for source in sources_list:
      epg_response = nw.getResponseForRegEx(source)
      if epg_response.isSucceeded:
        xmltv_url = re.search('(?i)italy xmltv</description>.*?<url>(.+?)</url>', epg_response.body) # (?i) = ignore case
        if xmltv_url != None:
          xmltv_url = xmltv_url.group(1)
          break

  if xmltv_url != None:
    xmltv_file = os.path.join(addon_userdata_path, 'epg.gz')
    _download_file(xmltv_url, xmltv_file)


def _download_m3u(addon_userdata_path):
  result = False

  new_m3u = ['#EXTM3U']

  _add_stream(new_m3u, addon_userdata_path, 'RaiUno.it', 'TV', 'Rai_1.png', 'Rai 1', 'http://mediapolis.rai.it/relinker/relinkerServlet.htm?cont=2606803')
  _add_stream(new_m3u, addon_userdata_path, 'RaiDue.it', 'TV', 'Rai_2.png', 'Rai 2', 'http://mediapolis.rai.it/relinker/relinkerServlet.htm?cont=180116')
  _add_stream(new_m3u, addon_userdata_path, 'RaiTre.it', 'TV', 'Rai_3.png', 'Rai 3', 'http://mediapolis.rai.it/relinker/relinkerServlet.htm?cont=180117')
  _add_stream(new_m3u, addon_userdata_path, 'Rete4.it', 'TV', 'Rete_4.png', 'Rete 4', 'http://live3.msf.ticdn.it/Content/HLS/Live/Channel(CH03HA)/Stream(04)/index.m3u8')
  _add_stream(new_m3u, addon_userdata_path, 'Canale5.it', 'TV', 'Canale_5.png', 'Canale 5', 'http://live1.msf.ticdn.it/Content/HLS/Live/Channel(CH01HA)/Stream(04)/index.m3u8')
  _add_stream(new_m3u, addon_userdata_path, 'Italia1.it', 'TV', 'Italia_1.png', 'Italia 1', 'http://live3.msf.ticdn.it/Content/HLS/Live/Channel(CH02HA)/Stream(04)/index.m3u8')
  _add_stream(new_m3u, addon_userdata_path, 'La7.it', 'TV', 'LA7.png', 'LA7', 'http://la7livehls-lh.akamaihd.net/i/livebkup_1@372883/master.m3u8')
  _add_stream(new_m3u, addon_userdata_path, 'Nove.it', 'TV', 'NOVE.png', 'NOVE', 'https://sbshdlu3-lh.akamaihd.net/i/sbshdlive_4@99403/master.m3u8', True)
  _add_stream(new_m3u, addon_userdata_path, 'Rai4.it', 'TV', 'Rai_4.png', 'Rai 4', 'http://mediapolis.rai.it/relinker/relinkerServlet.htm?cont=746966')
  _add_stream(new_m3u, addon_userdata_path, 'Iris.it', 'TV', 'Iris.png', 'Iris', 'http://live3.msf.ticdn.it/Content/HLS/Live/Channel(CH06HA)/Stream(04)/index.m3u8')
  _add_stream(new_m3u, addon_userdata_path, 'Rai5.it', 'TV', 'Rai_5.png', 'Rai 5', 'http://mediapolis.rai.it/relinker/relinkerServlet.htm?cont=72382')
  _add_stream(new_m3u, addon_userdata_path, 'RaisatCinema.it', 'TV', 'Rai_Movie.png', 'Rai Movie', 'http://mediapolis.rai.it/relinker/relinkerServlet.htm?cont=72381')
  _add_stream(new_m3u, addon_userdata_path, 'RaisatPremium.it', 'TV', 'Rai_Premium.png', 'Rai Premium', 'http://mediapolis.rai.it/relinker/relinkerServlet.htm?cont=72383')
  _add_stream(new_m3u, addon_userdata_path, 'Cielo.it', 'TV', 'Cielo.png', 'Cielo', 'http://skyianywhere2-i.akamaihd.net/hls/live/216865/cielo/playlist.m3u8')
  _add_stream(new_m3u, addon_userdata_path, 'ParamountChannel.it', 'TV', 'Paramount_Channel.png', 'Paramount Channel', 'http://viacomitalytest-lh.akamaihd.net/i/sbshdlive_1@195657/master.m3u8')
  _add_stream(new_m3u, addon_userdata_path, 'La7d.it', 'TV', 'LA7d.png', 'LA7d', 'http://se-mi1-5.se.itvmscvas.alice.cdn.interbusiness.it/liveas/cubovision/la7d/v7.m3u8', True)
  _add_stream(new_m3u, addon_userdata_path, 'LA5.it', 'TV', 'La5.png', 'La5', 'http://live3.msf.ticdn.it/Content/HLS/Live/Channel(CH04HA)/Stream(04)/index.m3u8')
  _add_stream(new_m3u, addon_userdata_path, 'RealTime.it', 'TV', 'RealTime.png', 'RealTime', 'https://sbshdlu3-lh.akamaihd.net/i/sbshdlive_4@99403/master.m3u8')
  _add_stream(new_m3u, addon_userdata_path, 'MediasetExtra.it', 'TV', 'Mediaset_Extra.png', 'Mediaset Extra', 'http://live3.msf.ticdn.it/Content/HLS/Live/Channel(CH09HA)/Stream(04)/index.m3u8')
  _add_stream(new_m3u, addon_userdata_path, 'Italia2.it', 'TV', 'Italia_2.png', 'Italia 2', 'http://live3.msf.ticdn.it/Content/HLS/Live/Channel(CH05HA)/Stream(04)/index.m3u8')
  _add_stream(new_m3u, addon_userdata_path, 'RTL102.5TV.it', 'TV', 'RTL_102.5.png', 'RTL 102.5', 'http://rtl-radio-stream.4mecloud.it/live-video/radiovisione/ngrp:radiovisione/chunklist_b784000.m3u8')
  _add_stream(new_m3u, addon_userdata_path, 'TopCrime.it', 'TV', 'TOP_Crime.png', 'TOP Crime', 'http://live3.msf.ticdn.it/Content/HLS/Live/Channel(CH07HA)/Stream(04)/index.m3u8')
  _add_stream(new_m3u, addon_userdata_path, 'RaiGulp.it', 'TV', 'Rai_Gulp.png', 'Rai Gulp', 'http://mediapolis.rai.it/relinker/relinkerServlet.htm?cont=4119')
  _add_stream(new_m3u, addon_userdata_path, 'RaiYoyo.it', 'TV', 'Rai_YoYo.png', 'Rai YoYo', 'http://mediapolis.rai.it/relinker/relinkerServlet.htm?cont=72384')
  _add_stream(new_m3u, addon_userdata_path, 'RaiNews.it', 'TV', 'RaiNews24.png', 'RaiNews24', 'http://mediapolis.rai.it/relinker/relinkerServlet.htm?cont=1')
  _add_stream(new_m3u, addon_userdata_path, 'TG24.it', 'TV', 'Sky_TG_24.png', 'Sky TG 24', 'http://skyianywhere2-i.akamaihd.net/hls/live/200275/tg24/playlist.m3u8')
  _add_stream(new_m3u, addon_userdata_path, 'DMAX.it', 'TV', 'DMAX.png', 'DMAX', 'https://sbshdlu3-lh.akamaihd.net/i/sbshdlive_4@99403/master.m3u8', True)
  _add_stream(new_m3u, addon_userdata_path, 'RaiStoria.it', 'TV', 'Rai_Storia.png', 'Rai Storia', 'http://mediapolis.rai.it/relinker/relinkerServlet.htm?cont=24269')
  _add_stream(new_m3u, addon_userdata_path, 'RaiSport1.it', 'TV', 'Rai_Sport_1.png', 'Rai Sport 1', 'http://mediapolis.rai.it/relinker/relinkerServlet.htm?cont=4145')
  _add_stream(new_m3u, addon_userdata_path, 'RaiSport2.it', 'TV', 'Rai_Sport_2.png', 'Rai Sport 2', 'http://mediapolis.rai.it/relinker/relinkerServlet.htm?cont=179975')
  _add_stream(new_m3u, addon_userdata_path, 'Sportitalia.it', 'TV', 'Sportitalia.png', 'Sportitalia', 'http://195.12.170.153:8003/play/IT-SportItalia', True)
  _add_stream(new_m3u, addon_userdata_path, 'SuperTennis.it', 'TV', 'SuperTennis.png', 'SuperTennis', 'http://livetok.flash.glb.ipercast.net/supertennis.tv-live/live/playlist.m3u8?id=4OUQM4V4Je_xs790uBB1ZfLZrW4_QmVjgtJP_o-Ek8bRJTFoji8(', True)
  _add_stream(new_m3u, addon_userdata_path, 'RaiScuola.it', 'TV', 'Rai_Scuola.png', 'Rai Scuola', 'http://mediapolis.rai.it/relinker/relinkerServlet.htm?cont=24268')
  _add_stream(new_m3u, addon_userdata_path, 'VirginTV.it', 'TV', 'Virgin_Radio_TV.png', 'Virgin Radio TV', 'rtmp://fms.105.net:1935/live/virgin1')
  _add_stream(new_m3u, addon_userdata_path, '???.it', 'TV', '???.png', '???', 'mmsh://mediatv2.topix.it/24RockOne66', True)
  _add_stream(new_m3u, addon_userdata_path, 'ResetRadio.it', 'Radio', 'Reset_Radio.png', 'Reset Radio', 'http://resetradiolive.ns0.it:8000', False, True)
  _add_stream(new_m3u, addon_userdata_path, 'FQRadio.it', 'Radio', 'FQ_Radio.png', 'FQ Radio', 'http://fqradio.ns0.it:8000/;audio.mp3', True, True)

  # Add Virgin radios.
  response = nw.getResponseJson('http://www.virginradio.it/custom_widget/finelco/ws_apps_vrg/getWebRadioList.jsp')
  if response.isSucceeded:
    _setRadiosListItem(response.body['webradios']['webradioChannel'], new_m3u, addon_userdata_path)
    _setRadiosListItem(response.body['webradios']['musicStar'], new_m3u, addon_userdata_path)

  new_m3u.append('#EXT-X-ENDLIST')

  new_m3u = '\n'.join(new_m3u)

  m3u_file = os.path.join(addon_userdata_path, 'iptv.m3u8')

  try:
    with open(m3u_file, 'r') as f:
      old_m3u = f.read()
  except:
    old_m3u = ''

  if old_m3u != new_m3u:
    try:
      with open(m3u_file, 'w') as f:
        f.write(new_m3u)
    except:
      pass
    else:
      result = True

  return result


def _add_stream(m3u, addon_userdata_path, id, group, logo, name, url_stream, is_disabled = False, is_radio = False):

  extinf = '#EXTINF:-1 tvg-id="{0}" group-title="{1}" tvg-logo="{2}" {3},{4}'
  if is_disabled:
    extinf = '##EXTINF:-1 tvg-id="{0}" group-title="{1}" tvg-logo="{2}" {3},{4}'
    url_stream = '#{0}'.format(url_stream)

  radio = ''
  if is_radio:
    radio = 'radio="true"'

  routes = logo.split('/')
  logo_name = routes[-1]
  logo_path = os.path.join(addon_userdata_path, logo_name)
  if len(routes) > 1:
    _download_file(logo, logo_path)
  else:
    url_logo = nw.addon.getSetting('url_tv_logos')
    if url_logo[-1] == '/':
      url_logo = '{0}{1}'.format(url_logo, logo_name)
    else:
      url_logo = '{0}/{1}'.format(url_logo, logo_name)
    _download_file(url_logo, logo_path)

  m3u.append(extinf.format(id, group, logo_name, radio, name))
  m3u.append(url_stream)


def _download_file(from_path, to_path):
  with closing(requests.get(from_path, stream = True)) as r:
    if r.status_code == 200 and ('application/' in r.headers['content-type'] or 'image/png' in r.headers['content-type']) and int(r.headers['content-length']) > 1024:
      try:
        with open(to_path, 'wb') as f:
          for chunk in r.iter_content(chunk_size = 1024):
            if chunk:
              f.write(chunk)
            else:
              break
      except:
        pass


def _setRadiosListItem(radios, new_m3u, addon_userdata_path):
  for radio in radios:
    name = radio['titolo']
    id_stream = '{0}.it'.format(name.replace(' ', ''))
    _add_stream(new_m3u, addon_userdata_path, id_stream, 'Radio', radio['immagine']['smartTv'], name, radio['streaming']['iOS'], False, True)


def _getUserDataPath():
  _base_path = nw.addon.getAddonInfo('path')
  _base_path = _base_path.split(os.sep)
  _base_path = os.sep.join(_base_path[:-2])
  return os.path.join(_base_path, 'userdata', 'addon_data')


def _getAddonUserDataPath(base_path):
  return os.path.join(base_path, nw.addon.getAddonInfo('id'))


def doupdate():
  base_path = _getUserDataPath()
  addon_userdata_path = _getAddonUserDataPath(base_path)
  _download_epg(addon_userdata_path)
  _download_m3u(addon_userdata_path)
  nw.addon.setSetting('update_date', str(datetime.today()))
  nw.showNotification(nw.getTranslation(30002), 15000)


# Entry point.
if len(sys.argv) > 1:

  if sys.argv[1] == 'setupiptv':
    if xbmcgui.Dialog().yesno(nw.addonName, nw.getTranslation(30003)):

      base_path = _getUserDataPath()
      addon_userdata_path = _getAddonUserDataPath(base_path)
      iptvsimple_userdata_path = os.path.join(base_path, 'pvr.iptvsimple')
      iptv_simple_dir = ''

      if os.path.isdir(iptvsimple_userdata_path):
        iptv_simple_dir = os.path.join(iptvsimple_userdata_path, 'settings.xml')

        if os.path.exists(iptv_simple_dir):
          os.rename(iptv_simple_dir, '{0}.old'.format(iptv_simple_dir))
      else:
        os.makedirs(iptvsimple_userdata_path)
        iptv_simple_dir = os.path.join(iptvsimple_userdata_path, 'settings.xml')

      path = os.path.join(addon_userdata_path, '')

      new_settings = ['<settings>']
      new_settings.append('<setting id="epgCache" value="true" />')
      new_settings.append('<setting id="epgPath" value="{0}epg.gz" />'.format(path))
      new_settings.append('<setting id="epgPathType" value="0" />')
      new_settings.append('<setting id="epgTSOverride" value="false" />')
      new_settings.append('<setting id="epgTimeShift" value="0.000000" />')
      new_settings.append('<setting id="epgUrl" value="" />')
      new_settings.append('<setting id="logoBaseUrl" value="" />')
      new_settings.append('<setting id="logoPath" value="{0}" />'.format(path))
      new_settings.append('<setting id="logoPathType" value="0" />')
      new_settings.append('<setting id="m3uCache" value="true" />')
      new_settings.append('<setting id="m3uPath" value="{0}iptv.m3u8" />'.format(path))
      new_settings.append('<setting id="m3uPathType" value="0" />')
      new_settings.append('<setting id="m3uUrl" value="" />')
      new_settings.append('<setting id="sep1" value="" />')
      new_settings.append('<setting id="sep2" value="" />')
      new_settings.append('<setting id="sep3" value="" />')
      new_settings.append('<setting id="startNum" value="1" />')
      new_settings.append('</settings>')

      new_settings = '\n'.join(new_settings)

      try:
        with open(iptv_simple_dir, 'w') as f:
          f.write(new_settings)
      except:
        pass

      nw.showNotification(nw.getTranslation(30004), 10000)

  elif sys.argv[1] == 'manualupdate':
    if xbmcgui.Dialog().yesno(nw.addonName, nw.getTranslation(30005)):
      doupdate()

elif len(sys.argv) == 1 and sys.argv[0] == 'default.py':
  nw.addon.openSettings()
