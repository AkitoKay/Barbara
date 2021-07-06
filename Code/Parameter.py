class Parameter:


    media_tabel_identifier = {'Bücher': '`literature`',
                            'Filme': '`movies`',
                            'Musik': '`music`'}

    media_search_columns = dict(Titel='`titel`',
                                Artist='`author`',
                                Herausgeber='`publisher`',
                                Jahr='`published`')

    media_column_identifier = {'id': '`id`',
                              'title': '`titel`',
                              'artist': '`author`',
                              'publisher': '`publisher`',
                              'release': '`published`',
                              'placement_id': '`id_shelf`'}

    lend_column_identifier = dict(id = '`id`',
                                  media_id = '`id_media`',
                                  customer_id = '`id_customer`',
                                  lend_date = '`date_output`',
                                  return_date = '`date_input`',
                                  media_type = '`type`')

    media_type_identifier = {'1': 'Bücher',
                             '2': 'Musik',
                             '3': 'Filme'}

    book_label_names = {'title': 'Titel:',
                         'artist': 'Autor:',
                         'publisher': 'Verlag:',
                         'release': 'Veröffentlichung:'}


    music_label_names = {'title': 'Titel:',
                         'artist': 'Künstler:',
                         'publisher': 'Label:',
                         'release': 'Veröffentlichung:'}

    movie_label_names = {'title': 'Titel:',
                         'artist': 'Regisseur:',
                         'publisher': 'Filmstudio:',
                         'release': 'Veröffentlichung:'}


