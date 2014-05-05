$(document).ready(function () {
    var buildGal = function (self) {
        var fancy = function () {
            var play = self.options.autoPlay;

            $('body').find('a.previmages,a.nextimages').remove();

            self.active.parents('li:first').prevAll().each(function () {
                var href = $(this).find('img').data('clickThrough');
                $('body').prepend($('<a>').attr({
                    'href': href,
                    'class': 'previmages',
                    'rel': 'gallery'
                }).css('display', 'none'));
            });

            self.active.parents('li:first').nextAll().each(function () {
                var href = $(this).find('img').data('clickThrough');
                $('body').append($('<a>').attr({
                    'href': href,
                    'class': 'nextimages',
                    'rel': 'gallery'
                }).css('display', 'none'));
            });

            self.anchor.attr('rel', 'gallery');

            $('a[rel=gallery]').fancybox({
                helpers: {
                    title: {
                        type: 'outside'
                    },
                    thumbs: {
                        width: 80,
                        height: 80
                    }
                },
                onStart: function () {
                    if (play) {
                        self.imgPlay.trigger('click');
                    }
                }
            });
        }

        self.anchor.bind('click', fancy);
        fancy();
    };

    $(".gallery").PikaChoose({
        buildFinished: buildGal,
        autoPlay: false,
        thumbOpacity: 1,
        showCaption: false,
        carousel: true
        // carouselOptions: {
        //     wrap: 'circular'
        // }
    });
});