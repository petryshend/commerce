INSERT INTO auctions_category (name) values ('Fashion');
INSERT INTO auctions_category (name) values ('Toys');
INSERT INTO auctions_category (name) values ('Electronics');
INSERT INTO auctions_category (name) values ('Home');

INSERT INTO auctions_listing (title, description, starting_bid)
VALUES (
    'First listing',
    'Lorem ipsum dolor sit amet, consectetur adipisicing elit. Aspernatur aut beatae consequuntur corporis cum earum eius excepturi exercitationem facere illum iure laboriosam nostrum officia officiis repudiandae soluta tempora, tempore, voluptates.',
    10
    );
INSERT INTO auctions_listing (title, description, starting_bid, category_id, image_url)
VALUES (
    'Second listing',
    'Lorem ipsum dolor sit amet, consectetur adipisicing elit. Aspernatur aut beatae consequuntur corporis cum earum eius excepturi exercitationem facere illum iure laboriosam nostrum officia officiis repudiandae soluta tempora, tempore, voluptates.',
    10,
    (SELECT id FROM auctions_category WHERE name = 'Home'),
    'http://lorempixel.com/400/400/'
    );
INSERT INTO auctions_listing (title, description, starting_bid, category_id, image_url)
VALUES (
    'Third listing',
    'Lorem ipsum dolor sit amet, consectetur adipisicing elit. Aspernatur aut beatae consequuntur corporis cum earum eius excepturi exercitationem facere illum iure laboriosam nostrum officia officiis repudiandae soluta tempora, tempore, voluptates.',
    10,
    (SELECT id FROM auctions_category WHERE name = 'Home'),
    'http://lorempixel.com/400/400/'
    );