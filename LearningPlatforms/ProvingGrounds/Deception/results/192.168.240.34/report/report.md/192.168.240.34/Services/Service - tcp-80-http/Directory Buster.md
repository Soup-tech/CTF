```bash
feroxbuster -u http://192.168.240.34:80/ -t 10 -w /root/.config/AutoRecon/wordlists/dirbuster.txt -x "txt,html,php,asp,aspx,jsp" -v -k -n -q -e -o "/home/kali/Documents/CTF/LearningPlatforms/ProvingGrounds/Deception/results/192.168.240.34/scans/tcp80/tcp_80_http_feroxbuster_dirbuster.txt"
```

[/home/kali/Documents/CTF/LearningPlatforms/ProvingGrounds/Deception/results/192.168.240.34/scans/tcp80/tcp_80_http_feroxbuster_dirbuster.txt](file:///home/kali/Documents/CTF/LearningPlatforms/ProvingGrounds/Deception/results/192.168.240.34/scans/tcp80/tcp_80_http_feroxbuster_dirbuster.txt):

```
200      GET       15l       74w     3338c http://192.168.240.34/icons/ubuntu-logo.png
403      GET        9l       28w      279c http://192.168.240.34/.hta
403      GET        9l       28w      279c http://192.168.240.34/.htaccess
403      GET        9l       28w      279c http://192.168.240.34/.hta.txt
403      GET        9l       28w      279c http://192.168.240.34/.htpasswd
403      GET        9l       28w      279c http://192.168.240.34/.hta.html
403      GET        9l       28w      279c http://192.168.240.34/.htaccess.txt
403      GET        9l       28w      279c http://192.168.240.34/.htpasswd.txt
403      GET        9l       28w      279c http://192.168.240.34/.htaccess.html
403      GET        9l       28w      279c http://192.168.240.34/.hta.php
403      GET        9l       28w      279c http://192.168.240.34/.htpasswd.html
403      GET        9l       28w      279c http://192.168.240.34/.hta.asp
403      GET        9l       28w      279c http://192.168.240.34/.htaccess.php
403      GET        9l       28w      279c http://192.168.240.34/.htpasswd.php
403      GET        9l       28w      279c http://192.168.240.34/.hta.aspx
403      GET        9l       28w      279c http://192.168.240.34/.htaccess.asp
403      GET        9l       28w      279c http://192.168.240.34/.htpasswd.asp
403      GET        9l       28w      279c http://192.168.240.34/.htpasswd.aspx
403      GET        9l       28w      279c http://192.168.240.34/.htaccess.aspx
403      GET        9l       28w      279c http://192.168.240.34/.hta.jsp
403      GET        9l       28w      279c http://192.168.240.34/.htaccess.jsp
403      GET        9l       28w      279c http://192.168.240.34/.htpasswd.jsp
200      GET      375l      981w    11026c http://192.168.240.34/index.html
301      GET        9l       28w      321c http://192.168.240.34/javascript => http://192.168.240.34/javascript/
301      GET        9l       28w      321c http://192.168.240.34/phpmyadmin => http://192.168.240.34/phpmyadmin/
403      GET        9l       28w      279c http://192.168.240.34/server-status
301      GET        9l       28w      320c http://192.168.240.34/wordpress => http://192.168.240.34/wordpress/
200      GET      375l      981w    11026c http://192.168.240.34/index.html
301      GET        9l       28w      320c http://192.168.240.34/wordpress => http://192.168.240.34/wordpress/
301      GET        0l        0w        0c http://192.168.240.34/wordpress/index.php => http://192.168.240.34/wordpress/
301      GET        9l       28w      331c http://192.168.240.34/wordpress/wp-content => http://192.168.240.34/wordpress/wp-content/
200      GET        0l        0w        0c http://192.168.240.34/wordpress/wp-content/index.php
301      GET        9l       28w      338c http://192.168.240.34/wordpress/wp-content/themes => http://192.168.240.34/wordpress/wp-content/themes/
200      GET        0l        0w        0c http://192.168.240.34/wordpress/wp-content/themes/index.php
301      GET        9l       28w      339c http://192.168.240.34/wordpress/wp-content/uploads => http://192.168.240.34/wordpress/wp-content/uploads/
200      GET       86l      288w     4914c http://192.168.240.34/wordpress/wp-login.php
301      GET        9l       28w      321c http://192.168.240.34/javascript => http://192.168.240.34/javascript/
200      GET      385l     3179w    19935c http://192.168.240.34/wordpress/license.txt
301      GET        9l       28w      339c http://192.168.240.34/wordpress/wp-content/plugins => http://192.168.240.34/wordpress/wp-content/plugins/
200      GET        0l        0w        0c http://192.168.240.34/wordpress/wp-content/plugins/index.php
301      GET        9l       28w      332c http://192.168.240.34/wordpress/wp-includes => http://192.168.240.34/wordpress/wp-includes/
301      GET        9l       28w      339c http://192.168.240.34/wordpress/wp-includes/images => http://192.168.240.34/wordpress/wp-includes/images/
500      GET        0l        0w        0c http://192.168.240.34/wordpress/wp-includes/rss.php
200      GET        0l        0w        0c http://192.168.240.34/wordpress/wp-includes/category.php
500      GET        0l        0w        0c http://192.168.240.34/wordpress/wp-includes/media.php
301      GET        9l       28w      345c http://192.168.240.34/wordpress/wp-includes/images/media => http://192.168.240.34/wordpress/wp-includes/images/media/
200      GET        0l        0w        0c http://192.168.240.34/wordpress/wp-includes/user.php
200      GET        0l        0w        0c http://192.168.240.34/wordpress/wp-includes/feed.php
200      GET        0l        0w        0c http://192.168.240.34/wordpress/wp-includes/version.php
500      GET        0l        0w        0c http://192.168.240.34/wordpress/wp-includes/registration.php
200      GET        0l        0w        0c http://192.168.240.34/wordpress/wp-includes/post.php
200      GET        0l        0w        0c http://192.168.240.34/wordpress/wp-includes/comment.php
301      GET        9l       28w      347c http://192.168.240.34/wordpress/wp-includes/images/smilies => http://192.168.240.34/wordpress/wp-includes/images/smilies/
301      GET        9l       28w      336c http://192.168.240.34/wordpress/wp-includes/css => http://192.168.240.34/wordpress/wp-includes/css/
200      GET        0l        0w        0c http://192.168.240.34/wordpress/wp-includes/template.php
500      GET        0l        0w        0c http://192.168.240.34/wordpress/wp-includes/date.php
500      GET        0l        0w        0c http://192.168.240.34/wordpress/wp-includes/update.php
301      GET        9l       28w      335c http://192.168.240.34/wordpress/wp-includes/js => http://192.168.240.34/wordpress/wp-includes/js/
200      GET       98l      838w     7368c http://192.168.240.34/wordpress/readme.html
200      GET        2l        3w       22c http://192.168.240.34/wordpress/robots.txt
200      GET       20l       44w      418c http://192.168.240.34/wordpress/robots.html
200      GET        0l        0w        0c http://192.168.240.34/wordpress/wp-includes/query.php
200      GET        0l        0w        0c http://192.168.240.34/wordpress/wp-includes/taxonomy.php
200      GET        0l        0w        0c http://192.168.240.34/wordpress/wp-includes/cache.php
200      GET        0l        0w        0c http://192.168.240.34/wordpress/wp-includes/theme.php
301      GET        9l       28w      339c http://192.168.240.34/wordpress/wp-includes/blocks => http://192.168.240.34/wordpress/wp-includes/blocks/
200      GET        0l        0w        0c http://192.168.240.34/wordpress/wp-includes/blocks.php
500      GET        0l        0w        0c http://192.168.240.34/wordpress/wp-includes/blocks/search.php
500      GET        0l        0w        0c http://192.168.240.34/wordpress/wp-includes/blocks/rss.php
500      GET        0l        0w        0c http://192.168.240.34/wordpress/wp-includes/blocks/archives.php
500      GET        0l        0w        0c http://192.168.240.34/wordpress/wp-includes/blocks/calendar.php
500      GET        0l        0w        0c http://192.168.240.34/wordpress/wp-includes/blocks/categories.php
200      GET        0l        0w        0c http://192.168.240.34/wordpress/wp-includes/http.php
200      GET        0l        0w        0c http://192.168.240.34/wordpress/wp-includes/meta.php
301      GET        9l       28w      340c http://192.168.240.34/wordpress/wp-includes/widgets => http://192.168.240.34/wordpress/wp-includes/widgets/
200      GET        0l        0w        0c http://192.168.240.34/wordpress/wp-includes/widgets.php
301      GET        9l       28w      341c http://192.168.240.34/wordpress/wp-includes/css/dist => http://192.168.240.34/wordpress/wp-includes/css/dist/
200      GET        0l        0w        0c http://192.168.240.34/wordpress/wp-includes/bookmark.php
200      GET        0l        0w        0c http://192.168.240.34/wordpress/wp-includes/cron.php
301      GET        9l       28w      340c http://192.168.240.34/wordpress/wp-includes/js/dist => http://192.168.240.34/wordpress/wp-includes/js/dist/
301      GET        9l       28w      338c http://192.168.240.34/wordpress/wp-includes/fonts => http://192.168.240.34/wordpress/wp-includes/fonts/
301      GET        9l       28w      342c http://192.168.240.34/wordpress/wp-includes/customize => http://192.168.240.34/wordpress/wp-includes/customize/
500      GET        0l        0w        0c http://192.168.240.34/wordpress/wp-includes/blocks/block.php
200      GET        0l        0w        0c http://192.168.240.34/wordpress/wp-includes/plugin.php
200      GET        5l       15w      135c http://192.168.240.34/wordpress/wp-trackback.php
500      GET        0l        0w        0c http://192.168.240.34/wordpress/wp-includes/functions.php
301      GET        9l       28w      345c http://192.168.240.34/wordpress/wp-includes/certificates => http://192.168.240.34/wordpress/wp-includes/certificates/
200      GET        0l        0w        0c http://192.168.240.34/wordpress/wp-includes/load.php
500      GET        0l        0w        0c http://192.168.240.34/wordpress/wp-content/plugins/hello.php
200      GET        0l        0w        0c http://192.168.240.34/wordpress/wp-includes/capabilities.php
301      GET        9l       28w      344c http://192.168.240.34/wordpress/wp-content/uploads/2020 => http://192.168.240.34/wordpress/wp-content/uploads/2020/
301      GET        9l       28w      329c http://192.168.240.34/wordpress/wp-admin => http://192.168.240.34/wordpress/wp-admin/
301      GET        9l       28w      336c http://192.168.240.34/wordpress/wp-admin/images => http://192.168.240.34/wordpress/wp-admin/images/
302      GET        0l        0w        0c http://192.168.240.34/wordpress/wp-admin/index.php => http://localhost/wordpress/wp-login.php?redirect_to=http%3A%2F%2F192.168.240.34%2Fwordpress%2Fwp-admin%2Findex.php&reauth=1
302      GET        0l        0w        0c http://192.168.240.34/wordpress/wp-admin/about.php => http://localhost/wordpress/wp-login.php?redirect_to=http%3A%2F%2F192.168.240.34%2Fwordpress%2Fwp-admin%2Fabout.php&reauth=1
302      GET        0l        0w        0c http://192.168.240.34/wordpress/wp-admin/privacy.php => http://localhost/wordpress/wp-login.php?redirect_to=http%3A%2F%2F192.168.240.34%2Fwordpress%2Fwp-admin%2Fprivacy.php&reauth=1
302      GET        0l        0w        0c http://192.168.240.34/wordpress/wp-admin/media.php => http://localhost/wordpress/wp-login.php?redirect_to=http%3A%2F%2F192.168.240.34%2Fwordpress%2Fwp-admin%2Fmedia.php&reauth=1
302      GET        0l        0w        0c http://192.168.240.34/wordpress/wp-admin/profile.php => http://localhost/wordpress/wp-login.php?redirect_to=http%3A%2F%2F192.168.240.34%2Fwordpress%2Fwp-admin%2Fprofile.php&reauth=1
301      GET        9l       28w      334c http://192.168.240.34/wordpress/wp-admin/user => http://192.168.240.34/wordpress/wp-admin/user/
302      GET        0l        0w        0c http://192.168.240.34/wordpress/wp-admin/themes.php => http://localhost/wordpress/wp-login.php?redirect_to=http%3A%2F%2F192.168.240.34%2Fwordpress%2Fwp-admin%2Fthemes.php&reauth=1
302      GET        0l        0w        0c http://192.168.240.34/wordpress/wp-admin/user/about.php => http://localhost/wordpress/wp-login.php?redirect_to=http%3A%2F%2F192.168.240.34%2Fwordpress%2Fwp-admin%2Fuser%2Fabout.php&reauth=1
302      GET        0l        0w        0c http://192.168.240.34/wordpress/wp-admin/tools.php => http://localhost/wordpress/wp-login.php?redirect_to=http%3A%2F%2F192.168.240.34%2Fwordpress%2Fwp-admin%2Ftools.php&reauth=1
302      GET        0l        0w        0c http://192.168.240.34/wordpress/wp-admin/user/privacy.php => http://localhost/wordpress/wp-login.php?redirect_to=http%3A%2F%2F192.168.240.34%2Fwordpress%2Fwp-admin%2Fuser%2Fprivacy.php&reauth=1
302      GET        0l        0w        0c http://192.168.240.34/wordpress/wp-admin/user/index.php => http://localhost/wordpress/wp-login.php?redirect_to=http%3A%2F%2F192.168.240.34%2Fwordpress%2Fwp-admin%2Fuser%2Findex.php&reauth=1
302      GET        0l        0w        0c http://192.168.240.34/wordpress/wp-admin/users.php => http://localhost/wordpress/wp-login.php?redirect_to=http%3A%2F%2F192.168.240.34%2Fwordpress%2Fwp-admin%2Fusers.php&reauth=1
302      GET        0l        0w        0c http://192.168.240.34/wordpress/wp-admin/user/profile.php => http://localhost/wordpress/wp-login.php?redirect_to=http%3A%2F%2F192.168.240.34%2Fwordpress%2Fwp-admin%2Fuser%2Fprofile.php&reauth=1
302      GET        0l        0w        0c http://192.168.240.34/wordpress/wp-admin/admin.php => http://localhost/wordpress/wp-login.php?redirect_to=http%3A%2F%2F192.168.240.34%2Fwordpress%2Fwp-admin%2Fadmin.php&reauth=1
302      GET        0l        0w        0c http://192.168.240.34/wordpress/wp-admin/link.php => http://localhost/wordpress/wp-login.php?redirect_to=http%3A%2F%2F192.168.240.34%2Fwordpress%2Fwp-admin%2Flink.php&reauth=1
500      GET        0l        0w        0c http://192.168.240.34/wordpress/wp-admin/menu.php
301      GET        9l       28w      337c http://192.168.240.34/wordpress/wp-admin/network => http://192.168.240.34/wordpress/wp-admin/network/
302      GET        0l        0w        0c http://192.168.240.34/wordpress/wp-admin/network.php => http://localhost/wordpress/wp-login.php?redirect_to=http%3A%2F%2F192.168.240.34%2Fwordpress%2Fwp-admin%2Fnetwork.php&reauth=1
302      GET        0l        0w        0c http://192.168.240.34/wordpress/wp-admin/post.php => http://localhost/wordpress/wp-login.php?redirect_to=http%3A%2F%2F192.168.240.34%2Fwordpress%2Fwp-admin%2Fpost.php&reauth=1
302      GET        0l        0w        0c http://192.168.240.34/wordpress/wp-admin/comment.php => http://localhost/wordpress/wp-login.php?redirect_to=http%3A%2F%2F192.168.240.34%2Fwordpress%2Fwp-admin%2Fcomment.php&reauth=1
302      GET        0l        0w        0c http://192.168.240.34/wordpress/wp-admin/upload.php => http://localhost/wordpress/wp-login.php?redirect_to=http%3A%2F%2F192.168.240.34%2Fwordpress%2Fwp-admin%2Fupload.php&reauth=1
302      GET        0l        0w        0c http://192.168.240.34/wordpress/wp-admin/network/about.php => http://localhost/wordpress/wp-login.php?redirect_to=http%3A%2F%2F192.168.240.34%2Fwordpress%2Fwp-admin%2Fnetwork%2Fabout.php&reauth=1
302      GET        0l        0w        0c http://192.168.240.34/wordpress/wp-admin/network/privacy.php => http://localhost/wordpress/wp-login.php?redirect_to=http%3A%2F%2F192.168.240.34%2Fwordpress%2Fwp-admin%2Fnetwork%2Fprivacy.php&reauth=1
302      GET        0l        0w        0c http://192.168.240.34/wordpress/wp-admin/user/admin.php => http://localhost/wordpress/wp-login.php?redirect_to=http%3A%2F%2F192.168.240.34%2Fwordpress%2Fwp-admin%2Fuser%2Fadmin.php&reauth=1
500      GET        0l        0w        0c http://192.168.240.34/wordpress/wp-admin/user/menu.php
302      GET        0l        0w        0c http://192.168.240.34/wordpress/wp-admin/network/index.php => http://localhost/wordpress/wp-login.php?redirect_to=http%3A%2F%2F192.168.240.34%2Fwordpress%2Fwp-admin%2Fnetwork%2Findex.php&reauth=1
500      GET        0l        0w        0c http://192.168.240.34/wordpress/wp-includes/locale.php
302      GET        0l        0w        0c http://192.168.240.34/wordpress/wp-admin/network/profile.php => http://localhost/wordpress/wp-login.php?redirect_to=http%3A%2F%2F192.168.240.34%2Fwordpress%2Fwp-admin%2Fnetwork%2Fprofile.php&reauth=1
302      GET        0l        0w        0c http://192.168.240.34/wordpress/wp-admin/plugins.php => http://localhost/wordpress/wp-login.php?redirect_to=http%3A%2F%2F192.168.240.34%2Fwordpress%2Fwp-admin%2Fplugins.php&reauth=1
302      GET        0l        0w        0c http://192.168.240.34/wordpress/wp-admin/network/themes.php => http://localhost/wordpress/wp-login.php?redirect_to=http%3A%2F%2F192.168.240.34%2Fwordpress%2Fwp-admin%2Fnetwork%2Fthemes.php&reauth=1
301      GET        9l       28w      333c http://192.168.240.34/wordpress/wp-admin/css => http://192.168.240.34/wordpress/wp-admin/css/
302      GET        0l        0w        0c http://192.168.240.34/wordpress/wp-admin/network/users.php => http://localhost/wordpress/wp-login.php?redirect_to=http%3A%2F%2F192.168.240.34%2Fwordpress%2Fwp-admin%2Fnetwork%2Fusers.php&reauth=1
302      GET        0l        0w        0c http://192.168.240.34/wordpress/wp-admin/edit.php => http://localhost/wordpress/wp-login.php?redirect_to=http%3A%2F%2F192.168.240.34%2Fwordpress%2Fwp-admin%2Fedit.php&reauth=1
302      GET        0l        0w        0c http://192.168.240.34/wordpress/wp-admin/credits.php => http://localhost/wordpress/wp-login.php?redirect_to=http%3A%2F%2F192.168.240.34%2Fwordpress%2Fwp-admin%2Fcredits.php&reauth=1
301      GET        9l       28w      338c http://192.168.240.34/wordpress/wp-admin/includes => http://192.168.240.34/wordpress/wp-admin/includes/
302      GET        0l        0w        0c http://192.168.240.34/wordpress/wp-admin/network/admin.php => http://localhost/wordpress/wp-login.php?redirect_to=http%3A%2F%2F192.168.240.34%2Fwordpress%2Fwp-admin%2Fnetwork%2Fadmin.php&reauth=1
500      GET        0l        0w        0c http://192.168.240.34/wordpress/wp-admin/network/menu.php
200      GET       17l       85w     1391c http://192.168.240.34/wordpress/wp-admin/install.php
200      GET        0l        0w        0c http://192.168.240.34/wordpress/wp-admin/includes/media.php
302      GET        0l        0w        0c http://192.168.240.34/wordpress/wp-admin/user/credits.php => http://localhost/wordpress/wp-login.php?redirect_to=http%3A%2F%2F192.168.240.34%2Fwordpress%2Fwp-admin%2Fuser%2Fcredits.php&reauth=1
200      GET        0l        0w        0c http://192.168.240.34/wordpress/wp-admin/includes/misc.php
200      GET        0l        0w        0c http://192.168.240.34/wordpress/wp-admin/includes/user.php
302      GET        0l        0w        0c http://192.168.240.34/wordpress/wp-admin/update.php => http://localhost/wordpress/wp-login.php?redirect_to=http%3A%2F%2F192.168.240.34%2Fwordpress%2Fwp-admin%2Fupdate.php&reauth=1
200      GET        0l        0w        0c http://192.168.240.34/wordpress/wp-admin/includes/image.php
500      GET        0l        0w        0c http://192.168.240.34/wordpress/wp-admin/includes/admin.php
302      GET        0l        0w        0c http://192.168.240.34/wordpress/wp-admin/network/plugins.php => http://localhost/wordpress/wp-login.php?redirect_to=http%3A%2F%2F192.168.240.34%2Fwordpress%2Fwp-admin%2Fnetwork%2Fplugins.php&reauth=1
301      GET        9l       28w      332c http://192.168.240.34/wordpress/wp-admin/js => http://192.168.240.34/wordpress/wp-admin/js/
302      GET        0l        0w        0c http://192.168.240.34/wordpress/wp-admin/network/sites.php => http://localhost/wordpress/wp-login.php?redirect_to=http%3A%2F%2F192.168.240.34%2Fwordpress%2Fwp-admin%2Fnetwork%2Fsites.php&reauth=1
500      GET        0l        0w        0c http://192.168.240.34/wordpress/wp-admin/includes/menu.php
302      GET        0l        0w        0c http://192.168.240.34/wordpress/wp-admin/term.php => http://localhost/wordpress/wp-login.php?redirect_to=http%3A%2F%2F192.168.240.34%2Fwordpress%2Fwp-admin%2Fterm.php&reauth=1
200      GET        0l        0w        0c http://192.168.240.34/wordpress/wp-admin/includes/network.php
302      GET        0l        0w        0c http://192.168.240.34/wordpress/wp-admin/network/edit.php => http://localhost/wordpress/wp-login.php?redirect_to=http%3A%2F%2F192.168.240.34%2Fwordpress%2Fwp-admin%2Fnetwork%2Fedit.php&reauth=1
302      GET        0l        0w        0c http://192.168.240.34/wordpress/wp-admin/network/credits.php => http://localhost/wordpress/wp-login.php?redirect_to=http%3A%2F%2F192.168.240.34%2Fwordpress%2Fwp-admin%2Fnetwork%2Fcredits.php&reauth=1
200      GET        0l        0w        0c http://192.168.240.34/wordpress/wp-admin/includes/post.php
200      GET       26l       93w     1491c http://192.168.240.34/wordpress/wp-admin/upgrade.php
200      GET        0l        0w        0c http://192.168.240.34/wordpress/wp-admin/includes/comment.php
302      GET        0l        0w        0c http://192.168.240.34/wordpress/wp-admin/network/update.php => http://localhost/wordpress/wp-login.php?redirect_to=http%3A%2F%2F192.168.240.34%2Fwordpress%2Fwp-admin%2Fnetwork%2Fupdate.php&reauth=1
500      GET        0l        0w        0c http://192.168.240.34/wordpress/wp-admin/includes/template.php
302      GET        0l        0w        0c http://192.168.240.34/wordpress/wp-admin/export.php => http://localhost/wordpress/wp-login.php?redirect_to=http%3A%2F%2F192.168.240.34%2Fwordpress%2Fwp-admin%2Fexport.php&reauth=1
200      GET        0l        0w        0c http://192.168.240.34/wordpress/wp-admin/includes/credits.php
302      GET        0l        0w        0c http://192.168.240.34/wordpress/wp-admin/options.php => http://localhost/wordpress/wp-login.php?redirect_to=http%3A%2F%2F192.168.240.34%2Fwordpress%2Fwp-admin%2Foptions.php&reauth=1
302      GET        0l        0w        0c http://192.168.240.34/wordpress/wp-admin/network/upgrade.php => http://localhost/wordpress/wp-login.php?redirect_to=http%3A%2F%2F192.168.240.34%2Fwordpress%2Fwp-admin%2Fnetwork%2Fupgrade.php&reauth=1
500      GET        0l        0w        0c http://192.168.240.34/wordpress/wp-admin/includes/file.php
200      GET        0l        0w        0c http://192.168.240.34/wordpress/wp-admin/includes/update.php
302      GET        0l        0w        0c http://192.168.240.34/wordpress/wp-admin/widgets.php => http://localhost/wordpress/wp-login.php?redirect_to=http%3A%2F%2F192.168.240.34%2Fwordpress%2Fwp-admin%2Fwidgets.php&reauth=1
500      GET        0l        0w        0c http://192.168.240.34/wordpress/wp-admin/includes/upgrade.php
200      GET        0l        0w        0c http://192.168.240.34/wordpress/wp-admin/includes/taxonomy.php
301      GET        9l       28w      337c http://192.168.240.34/wordpress/wp-includes/Text => http://192.168.240.34/wordpress/wp-includes/Text/

```
