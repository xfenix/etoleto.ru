/*
    Gallery

    Needs DOM likes this:
    ---
    <div class="product-gallery-big">
        <a href="#"><img src="{{ object.images.all.0.preview_big.url }}" class="product-gallery-big-image" alt="" /></a>
    </div>
    <ul class="product-gallery-tumbs">
        {% for img in object.images.all %}
        <li class="product-gallery-tumbs-line">
            <a href="{{ img.preview_big.url }}" class="product-gallery-tumbs-link {% if forloop.first %}active{% endif %}" data-origin="{{ img.image.url }}" data-index="{{ forloop.counter0 }}"><img src="{{ img.preview.url }}" class="product-gallery-tumbs-img" alt=""></a>
        {% endfor %}
    </ul>
    ---
    
    And global galleryJson var list like this:
    ---
    galleryJson = [{% for img in object.images.all %}{href: "{{ img.image.url }}", title: "{{ img.title }}"},{% endfor %}]
    ---
*/
$(function() {
    var gallery = $('.product-gallery'),
        bigImage = gallery.find('.product-gallery-big-image'),
        bigImageLink = bigImage.parent('a'),
        tumbs = gallery.find('.product-gallery-tumbs-link'),
        activeClass = 'active',
        currentIndex = 0,
        self;

    tumbs.on(
        'click',
        function() {
            self = $(this);
            tumbs.removeClass(activeClass);
            self.addClass(activeClass);
            currentIndex = self.data('index');
            bigImage.attr('src', self.attr('href'));
            return false;
        }
    );

    bigImageLink.on(
        'click',
        function() {
            $.fancybox.open(
                window.galleryJson,
                {
                    index: currentIndex,
                    helpers: {
                        thumbs: {
                            width: 80,
                            height: 80
                        }
                    }
                }
            );
            return false;
        }
    );
});
