class Parameter:


    media_tabel_identifier = dict(Bücher='literature',
                                  Filme='movies',
                                  Musik='music')
    
    media_type_identifier = {'1': 'Bücher',
                             '2': 'Musik',
                             '3': 'Filme'}
    
    media_search_columns = {'Titel': 'titel',
                            'Autor/Artist/Produzent': 'author',
                            'Verlag/Label/Studio': 'publisher',
                            'Veröffentlichungsdatum': 'published'}

    media_table_identifier = dict(media_id='id',
                                  title='titel',
                                  artist='author',
                                  publisher='publisher',
                                  release='published',
                                  placement_id='id_shelf')

    lend_column_identifier = dict(lend_id='id',
                                  media_id='id_media',
                                  customer_id='id_customer',
                                  lend_date='date_output',
                                  return_date='date_input',
                                  media_type='type')

    shelf_column_identifier = dict()

    floor_column_identifier = dict()

    people_column_identifier = dict()


    book_label_names = dict(l_title='Titel:',
                            l_artist='Autor:',
                            l_publisher='Verlag:',
                            l_release='Veröffentlichung:')

    music_label_names = dict(l_title='Titel:',
                             l_artist='Künstler:',
                             l_publisher='Label:',
                             l_release='Veröffentlichung:')

    movie_label_names = dict(l_title='Titel:',
                             l_artist='Regisseur:',
                             l_publisher='Filmstudio:',
                             l_release='Veröffentlichung:')

