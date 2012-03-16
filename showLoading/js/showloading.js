(function(){
    var zbShowLoading = new Class({
        _defaults: {
            'id' : null,
            'addClass': '',
            'beforeShow': function () {},
            'afterShow': function () {},
            'hPos': 'center',
            'vPos': 'center',
            'indicatorZIndex' : 5001,
            'overlayZIndex': 5000,
            'parent': '',
            'marginTop': 0,
            'marginLeft': 0,
            'overlayWidth': null,
            'overlayHeight': null
        },
        initialize: function (element, options) {
            console.debug("inizializza");

            options = $merge(this._defaults, options);

            this.options = options;

            if (this.options.id == null) {
                this.options.id = element.get('id');
            }

            this.element = element;

            this.loadingDiv = new Element('div');
            this.overlayDiv = new Element('div');

            this.indicatorID = this.options.indicatorID ? this.options.indicatorID : this.element.get('id');

            this.loadingDiv.setProperty('id','loading-indicator-' + this.indicatorID);
            this.loadingDiv.addClass('loading-indicator');

            if ( this.options.addClass ){
                this.loadingDiv.addClass(options.addClass);
            }

            // Create the overlay
            this.overlayDiv.setStyle('display','none');

            // Append to body, otherwise position() doesn't work on Webkit-based browsers
            this.overlayDiv.inject($(document.body),'bottom');


            // Set overlay classes
            this.overlayDiv.set('id','loading-indicator-' + this.indicatorID + '-overlay');
            this.overlayDiv.addClass('loading-indicator-overlay');

            if ( this.options.addClass ){
                this.overlayDiv.addClass(options.addClass + '-overlay');
            }

            // Set overlay position

            var overlay_width;
            var overlay_height;
            var border_top_width = this.element.getStyle('border-top-width');
            var border_left_width = this.element.getStyle('border-left-width');


            //
            // IE will return values like 'medium' as the default border,
            // but we need a number
            //
            border_top_width = isNaN(parseInt(border_top_width)) ? 0 : border_top_width;
            border_left_width = isNaN(parseInt(border_left_width)) ? 0 : border_left_width;

            var overlay_left_pos = this.element.getPosition().x + parseInt(border_left_width);
            var overlay_top_pos = this.element.getPosition().y + parseInt(border_top_width);


            if ( this.options.overlayWidth !== null ) {
                overlay_width = options.overlayWidth;
            }
            else {
                overlay_width = parseInt(this.element.getStyle('width').toInt()) + parseInt(this.element.getStyle('padding-right')) + parseInt(this.element.getStyle('padding-left'));
            }

            if ( this.options.overlayHeight !== null ) {
                overlay_height = options.overlayWidth;
            }
            else {
                overlay_height = parseInt(this.element.getStyle('height').toInt()) + parseInt(this.element.getStyle('padding-top')) + parseInt(this.element.getStyle('padding-bottom'));
            }

            this.overlayDiv.setStyle('width', overlay_width.toString() + 'px');
            this.overlayDiv.setStyle('height', overlay_height.toString() + 'px');

            this.overlayDiv.setStyle('left', overlay_left_pos.toString() + 'px');
            this.overlayDiv.setStyle('position', 'absolute');

            this.overlayDiv.setStyle('top', overlay_top_pos.toString() + 'px' );
            this.overlayDiv.setStyle('z-index', this.options.overlayZIndex);

            // Set any custom overlay CSS
            if ( this.options.overlayCSS ) {
                this.overlayDiv.setStyle( this.options.overlayCSS );
            }

            // We have to append the element to the body first
            // or .width() won't work in Webkit-based browsers (e.g. Chrome, Safari)
            //
            this.loadingDiv.setStyle('display', 'none');
            this.loadingDiv.inject($(document.body),'bottom');

            this.loadingDiv.setStyle('position', 'absolute');
            this.loadingDiv.setStyle('z-index', this.options.indicatorZIndex);


            // Set top margin
            var indicatorTop = overlay_top_pos;
            if ( this.options.marginTop ) {
                indicatorTop += parseInt(this.options.marginTop);
            }

            var indicatorLeft = overlay_left_pos;

            if ( this.options.marginLeft ) {
                indicatorLeft += parseInt(this.options.marginTop);
            }

            // set horizontal position
            if ( this.options.hPos.toString().toLowerCase() == 'center' ) {
                this.loadingDiv.setStyle('left', (indicatorLeft + ((this.overlayDiv.getStyle('width').toInt() - parseInt(this.loadingDiv.getStyle('width').toInt())) / 2)).toString()  + 'px');
            }
            else if ( this.options.hPos.toString().toLowerCase() == 'left' ) {
                this.loadingDiv.setStyle('left', (indicatorLeft + parseInt(this.overlayDiv.getStyle('margin-left'))).toString() + 'px');
            }
            else if ( this.options.hPos.toString().toLowerCase() == 'right' ) {
                this.loadingDiv.setStyle('left', (indicatorLeft + (this.overlayDiv.getStyle('width').toInt() - parseInt(this.loadingDiv.getStyle('width').toInt()))).toString()  + 'px');
            }
            else {
                this.loadingDiv.setStyle('left', (indicatorLeft + parseInt(this.options.hPos)).toString() + 'px');
            }

            //
            // set vertical position
            //
            if ( this.options.vPos.toString().toLowerCase() == 'center' ) {
                this.loadingDiv.setStyle('top', (indicatorTop + ((this.overlayDiv.getStyle('height').toInt() - parseInt(this.loadingDiv.getStyle('height').toInt())) / 2)).toString()  + 'px');
            }
            else if ( this.options.vPos.toString().toLowerCase() == 'top' ) {
                this.loadingDiv.setStyle('top', indicatorTop.toString() + 'px');
            }
            else if ( this.options.vPos.toString().toLowerCase() == 'bottom' ) {
                this.loadingDiv.setStyle('top', (indicatorTop + (this.overlayDiv.getStyle('height').toInt() - parseInt(this.loadingDiv.getStyle('height').toInt()))).toString()  + 'px');
            }
            else {
                this.loadingDiv.setStyle('top', (indicatorTop + parseInt(this.options.vPos)).toString() + 'px' );
            }

            // Set any custom css for loading indicator
            if ( this.options.css ) {
                this.loadingDiv.setStyles( this.options.css );
            }

            // Set up callback options
            var callback_options ={
                'overlay': this.overlayDiv,
                'indicator': this.loadingDiv,
                'element': this.element
            };

            // beforeShow callback
            if ( typeof(this.options.beforeShow) == 'function' ) {
                this.options.beforeShow( callback_options );
            }

            // Show the overlay
            this.overlayDiv.setStyle('display','block');

            // Show the loading indicator
            this.loadingDiv.setStyle('display','block');

            // afterShow callback
            if ( typeof(this.options.afterShow) == 'function' ) {
                this.options.afterShow( callback_options );
            }
        }
    });

    var zbHideLoading = new Class({
        _defaults: {
            'id': null,
            'className': 'zb-autocompleter',
            'delay': 300,
            'minLength': 3,
            'maxResults': 10,
            'maxHeight': 300,
            'source': '',
            'onCreate': function () {},
            'onSearch': function () {},
            'onSuggest': function () {},
            'onChange': function () {},
            'onBeforeShow': function() {},
            'onConfirm': function() {}
        },
        initialize: function (element, options) {
            console.debug("inizializza hideLoading");
            options = $merge(this._defaults, options);

            if (options.id == null) {
                options.id = element.get('id');
            }

            this.element = element;
            this.options = options;

            var indicatorID = this.options.indicatorID ? this.options.indicatorID : this.element.get('id');

            $(document.body).getElement('#loading-indicator-' + indicatorID).dispose();
            $(document.body).getElement('#loading-indicator-' + indicatorID + '-overlay' ).dispose();
        }
    });

    Element.implement({

        showLoading: function(options){
            var _zbShowLoading = this.get('showLoading');

            if(!_zbShowLoading)  _zbShowLoading = new zbShowLoading(this, options);

            return _zbShowLoading;

        },

        hideLoading: function(options){
            var _zbHideLoading = this.get('hideLoading');

            if(!_zbHideLoading)  _zbHideLoading = new zbHideLoading(this, options);

            return _zbHideLoading;
        }
    });

})();