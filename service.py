#!/usr/bin/python
import neverwise as nw, xbmc
import default as module
from datetime import datetime, timedelta


class LiveTV(object):

  def __init__(self):
    monitor = xbmc.Monitor()

    while not monitor.abortRequested():
      if monitor.waitForAbort(60):
        break
      if not xbmc.Player().isPlaying() or xbmc.getCondVisibility('Library.IsScanningVideo'):

        update_date = nw.addon.getSetting('update_date')
        update_date = nw.strptime(update_date, '%Y-%m-%d %H:%M:%S.%f')

        delta_date = datetime.today() - timedelta(days = 1)

        if update_date < delta_date:
          module.doupdate()


# Entry point.
#startTime = datetime.now()
ltv = LiveTV()
del ltv
#xbmc.log('{0} azione {1}'.format(nw.addonName, str(datetime.now() - startTime)))
