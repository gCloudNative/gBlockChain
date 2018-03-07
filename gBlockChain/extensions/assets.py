# -*- coding: utf-8 -*-

from flask_assets import Bundle, Environment


css_all = Bundle(
        'css/icons/fontawesome/styles.min.css',
        # 'css/icons/icomoon/icomoon_styles.css',
        'css/icomoon_styles.css',
        'css/bootstrap.css',
        'css/core.css',
        'css/components.css',
        'css/colors.css',
        'css/font_googleapis.css',
        'css/extras/hint.min.css',
        filters='cssmin', #compass
        output='gen/packed.css',
        debug=False)


js_all = Bundle(
        'js/core/libraries/jquery.min.js',
        'js/core/libraries/bootstrap.min.js',
        'js/core/libraries/jquery_ui/core.min.js',
        'js/core/libraries/jquery_ui/interactions.min.js',
        'js/plugins/loaders/pace.min.js',
        'js/plugins/loaders/blockui.min.js',
        'js/plugins/ui/nicescroll.min.js',
        'js/plugins/ui/drilldown.js',
        'js/plugins/forms/styling/switchery.min.js',
        'js/plugins/forms/styling/uniform.min.js',
        'js/plugins/forms/inputs/touchspin.min.js',
        'js/plugins/forms/editable/editable.min.js',
        'js/plugins/forms/selects/select2.min.js',
        'js/plugins/forms/selects/selectboxit.min.js',
        'js/plugins/forms/selects/bootstrap_multiselect.js',
        'js/plugins/forms/selects/bootstrap_select.min.js',
        'js/plugins/ui/moment/moment.min.js',
        'js/plugins/visualization/d3/d3.min.js',
        'js/plugins/visualization/d3/d3_tooltip.js',
        'js/plugins/pickers/daterangepicker.js',
        # 'js/plugins/tables/datatables/datatables.min.js',
        'js/plugins/tables/datatables/datatables.js',
        # 'js/plugins/tables/datatables/extensions/buttons.min.js',
        'js/plugins/uploaders/fileinput/plugins/purify.min.js',
        'js/plugins/uploaders/fileinput/plugins/sortable.min.js',
        'js/plugins/uploaders/fileinput/fileinput.min.js',
        'js/plugins/notifications/pnotify.min.js',
        'js/plugins/notifications/noty.min.js',
        'js/plugins/notifications/jgrowl.min.js',
        'js/plugins/extensions/contextmenu.js',
        'js/plugins/visualization/sparkline.min.js',
        'js/plugins/forms/wizards/steps.min.js',
        'js/core/libraries/jasny_bootstrap.min.js',
        'js/plugins/forms/validation/validate.min.js',
        'js/plugins/extensions/cookie.js',
        'js/core/app.js',
        'js/pages/colors_primary.js',
        'js/pages/datatables_extension_colvis.js',
        'js/pages/wizard_steps.js',
        'js/pages/form_select2.js',
        'js/pages/table_elements.js',
        filters='jsmin', #uglifyjs
        output='gen/packed.js',
        debug=False)

extension = Environment()
extension.register('js_all', js_all)
extension.register('css_all', css_all)
