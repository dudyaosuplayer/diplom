PGDMP         %            	    {            cnrprod-team-58619 .   15.4 (Ubuntu 15.4-201-yandex.54646.faaed79206)    15.4 [    �           0    0    ENCODING    ENCODING        SET client_encoding = 'UTF8';
                      false            �           0    0 
   STDSTRINGS 
   STDSTRINGS     (   SET standard_conforming_strings = 'on';
                      false            �           0    0 
   SEARCHPATH 
   SEARCHPATH     8   SELECT pg_catalog.set_config('search_path', '', false);
                      false            �           1262    16582    cnrprod-team-58619    DATABASE     v   CREATE DATABASE "cnrprod-team-58619" WITH TEMPLATE = template0 ENCODING = 'UTF8' LOCALE_PROVIDER = libc LOCALE = 'C';
 $   DROP DATABASE "cnrprod-team-58619";
                cnrprod-team-58619    false            �           0    0    DATABASE "cnrprod-team-58619"    ACL     r  REVOKE CONNECT,TEMPORARY ON DATABASE "cnrprod-team-58619" FROM PUBLIC;
GRANT TEMPORARY ON DATABASE "cnrprod-team-58619" TO PUBLIC;
GRANT CONNECT ON DATABASE "cnrprod-team-58619" TO mdb_odyssey;
GRANT CONNECT ON DATABASE "cnrprod-team-58619" TO monitor;
GRANT CONNECT ON DATABASE "cnrprod-team-58619" TO admin;
GRANT CONNECT ON DATABASE "cnrprod-team-58619" TO postgres;
                   cnrprod-team-58619    false    4023                        2615    27621    lg    SCHEMA        CREATE SCHEMA lg;
    DROP SCHEMA lg;
                cnrprod-team-58619    false                        2615    27837    prjct    SCHEMA        CREATE SCHEMA prjct;
    DROP SCHEMA prjct;
                cnrprod-team-58619    false                        2615    27827    usr    SCHEMA        CREATE SCHEMA usr;
    DROP SCHEMA usr;
                cnrprod-team-58619    false            �           0    0 4   FUNCTION pg_replication_origin_advance(text, pg_lsn)    ACL     a   GRANT ALL ON FUNCTION pg_catalog.pg_replication_origin_advance(text, pg_lsn) TO mdb_replication;
       
   pg_catalog          postgres    false    244            �           0    0 +   FUNCTION pg_replication_origin_create(text)    ACL     X   GRANT ALL ON FUNCTION pg_catalog.pg_replication_origin_create(text) TO mdb_replication;
       
   pg_catalog          postgres    false    237            �           0    0 )   FUNCTION pg_replication_origin_drop(text)    ACL     V   GRANT ALL ON FUNCTION pg_catalog.pg_replication_origin_drop(text) TO mdb_replication;
       
   pg_catalog          postgres    false    238            �           0    0 (   FUNCTION pg_replication_origin_oid(text)    ACL     U   GRANT ALL ON FUNCTION pg_catalog.pg_replication_origin_oid(text) TO mdb_replication;
       
   pg_catalog          postgres    false    239            �           0    0 6   FUNCTION pg_replication_origin_progress(text, boolean)    ACL     c   GRANT ALL ON FUNCTION pg_catalog.pg_replication_origin_progress(text, boolean) TO mdb_replication;
       
   pg_catalog          postgres    false    245            �           0    0 .   FUNCTION pg_replication_origin_session_reset()    ACL     [   GRANT ALL ON FUNCTION pg_catalog.pg_replication_origin_session_reset() TO mdb_replication;
       
   pg_catalog          postgres    false    241            �           0    0 2   FUNCTION pg_replication_origin_session_setup(text)    ACL     _   GRANT ALL ON FUNCTION pg_catalog.pg_replication_origin_session_setup(text) TO mdb_replication;
       
   pg_catalog          postgres    false    240            �           0    0 +   FUNCTION pg_replication_origin_xact_reset()    ACL     X   GRANT ALL ON FUNCTION pg_catalog.pg_replication_origin_xact_reset() TO mdb_replication;
       
   pg_catalog          postgres    false    243            �           0    0 K   FUNCTION pg_replication_origin_xact_setup(pg_lsn, timestamp with time zone)    ACL     x   GRANT ALL ON FUNCTION pg_catalog.pg_replication_origin_xact_setup(pg_lsn, timestamp with time zone) TO mdb_replication;
       
   pg_catalog          postgres    false    242            �           0    0    FUNCTION pg_stat_reset()    ACL     ?   GRANT ALL ON FUNCTION pg_catalog.pg_stat_reset() TO mdb_admin;
       
   pg_catalog          postgres    false    236            �            1259    27894 	   log_table    TABLE       CREATE TABLE lg.log_table (
    log_id integer NOT NULL,
    start_time timestamp without time zone NOT NULL,
    end_time timestamp without time zone,
    operation_type character varying(50),
    additional_info character varying(255),
    task_id integer,
    user_id integer
);
    DROP TABLE lg.log_table;
       lg         heap    cnrprod-team-58619    false    6            �            1259    27893    log_table_log_id_seq    SEQUENCE     �   CREATE SEQUENCE lg.log_table_log_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;
 '   DROP SEQUENCE lg.log_table_log_id_seq;
       lg          cnrprod-team-58619    false    220    6            �           0    0    log_table_log_id_seq    SEQUENCE OWNED BY     E   ALTER SEQUENCE lg.log_table_log_id_seq OWNED BY lg.log_table.log_id;
          lg          cnrprod-team-58619    false    219            �            1259    28205    assignee    TABLE     f   CREATE TABLE prjct.assignee (
    id integer NOT NULL,
    project_id integer,
    user_id integer
);
    DROP TABLE prjct.assignee;
       prjct         heap    cnrprod-team-58619    false    8            �            1259    28204    assignee_id_seq    SEQUENCE     �   CREATE SEQUENCE prjct.assignee_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;
 %   DROP SEQUENCE prjct.assignee_id_seq;
       prjct          cnrprod-team-58619    false    222    8            �           0    0    assignee_id_seq    SEQUENCE OWNED BY     A   ALTER SEQUENCE prjct.assignee_id_seq OWNED BY prjct.assignee.id;
          prjct          cnrprod-team-58619    false    221            �            1259    27875    comments    TABLE     �   CREATE TABLE prjct.comments (
    id integer NOT NULL,
    task_id integer,
    user_id integer,
    comment text,
    "timestamp" timestamp without time zone
);
    DROP TABLE prjct.comments;
       prjct         heap    cnrprod-team-58619    false    8            �            1259    27874    comments_id_seq    SEQUENCE     �   CREATE SEQUENCE prjct.comments_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;
 %   DROP SEQUENCE prjct.comments_id_seq;
       prjct          cnrprod-team-58619    false    8    218            �           0    0    comments_id_seq    SEQUENCE OWNED BY     A   ALTER SEQUENCE prjct.comments_id_seq OWNED BY prjct.comments.id;
          prjct          cnrprod-team-58619    false    217            �            1259    29223    projects    TABLE     �   CREATE TABLE prjct.projects (
    id integer NOT NULL,
    name character varying(255),
    description text,
    goals text,
    deadline date,
    status integer
);
    DROP TABLE prjct.projects;
       prjct         heap    cnrprod-team-58619    false    8            �            1259    28611    task    TABLE       CREATE TABLE prjct.task (
    id bigint,
    date_creation timestamp without time zone,
    due_date timestamp without time zone,
    status bigint,
    name text,
    description text,
    assignee_id bigint,
    parent_task_id bigint,
    project_id bigint
);
    DROP TABLE prjct.task;
       prjct         heap    cnrprod-team-58619    false    8            �            1259    29070    comment    TABLE     �   CREATE TABLE public.comment (
    id integer NOT NULL,
    user_id integer,
    task_id integer,
    "timestamp" timestamp without time zone,
    text character varying
);
    DROP TABLE public.comment;
       public         heap    cnrprod-team-58619    false            �            1259    29069    comment_id_seq    SEQUENCE     �   CREATE SEQUENCE public.comment_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;
 %   DROP SEQUENCE public.comment_id_seq;
       public          cnrprod-team-58619    false    234            �           0    0    comment_id_seq    SEQUENCE OWNED BY     A   ALTER SEQUENCE public.comment_id_seq OWNED BY public.comment.id;
          public          cnrprod-team-58619    false    233            �            1259    29021    project    TABLE     |   CREATE TABLE public.project (
    id integer NOT NULL,
    name character varying(255),
    status character varying(10)
);
    DROP TABLE public.project;
       public         heap    cnrprod-team-58619    false            �            1259    29020    project_id_seq    SEQUENCE     �   CREATE SEQUENCE public.project_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;
 %   DROP SEQUENCE public.project_id_seq;
       public          cnrprod-team-58619    false    227            �           0    0    project_id_seq    SEQUENCE OWNED BY     A   ALTER SEQUENCE public.project_id_seq OWNED BY public.project.id;
          public          cnrprod-team-58619    false    226            �            1259    29036    project_user_association    TABLE     ^   CREATE TABLE public.project_user_association (
    project_id integer,
    user_id integer
);
 ,   DROP TABLE public.project_user_association;
       public         heap    cnrprod-team-58619    false            �            1259    29050    task    TABLE       CREATE TABLE public.task (
    id integer NOT NULL,
    parent_id integer,
    body character varying,
    task_name character varying(140),
    "timestamp" timestamp without time zone,
    user_id integer,
    project_id integer,
    status character varying(10)
);
    DROP TABLE public.task;
       public         heap    cnrprod-team-58619    false            �            1259    29049    task_id_seq    SEQUENCE     �   CREATE SEQUENCE public.task_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;
 "   DROP SEQUENCE public.task_id_seq;
       public          cnrprod-team-58619    false    232            �           0    0    task_id_seq    SEQUENCE OWNED BY     ;   ALTER SEQUENCE public.task_id_seq OWNED BY public.task.id;
          public          cnrprod-team-58619    false    231            �            1259    29028    user    TABLE     3  CREATE TABLE public."user" (
    id integer NOT NULL,
    nickname character varying(64),
    email character varying(64),
    p_hash character varying(96),
    password character varying(24),
    cookie character varying(8),
    role character varying(24),
    register_date timestamp without time zone
);
    DROP TABLE public."user";
       public         heap    cnrprod-team-58619    false            �            1259    29027    user_id_seq    SEQUENCE     �   CREATE SEQUENCE public.user_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;
 "   DROP SEQUENCE public.user_id_seq;
       public          cnrprod-team-58619    false    229            �           0    0    user_id_seq    SEQUENCE OWNED BY     =   ALTER SEQUENCE public.user_id_seq OWNED BY public."user".id;
          public          cnrprod-team-58619    false    228            �            1259    28861    user    TABLE     �   CREATE TABLE usr."user" (
    id integer NOT NULL,
    full_name character varying(255),
    email character varying(255),
    role integer,
    hash_password character varying(255),
    cookie character varying(8)
);
    DROP TABLE usr."user";
       usr         heap    cnrprod-team-58619    false    7            �            1259    28860    user_id_seq    SEQUENCE     �   CREATE SEQUENCE usr.user_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;
    DROP SEQUENCE usr.user_id_seq;
       usr          cnrprod-team-58619    false    7    225            �           0    0    user_id_seq    SEQUENCE OWNED BY     7   ALTER SEQUENCE usr.user_id_seq OWNED BY usr."user".id;
          usr          cnrprod-team-58619    false    224            �           2604    27897    log_table log_id    DEFAULT     l   ALTER TABLE ONLY lg.log_table ALTER COLUMN log_id SET DEFAULT nextval('lg.log_table_log_id_seq'::regclass);
 ;   ALTER TABLE lg.log_table ALTER COLUMN log_id DROP DEFAULT;
       lg          cnrprod-team-58619    false    219    220    220            �           2604    28208    assignee id    DEFAULT     h   ALTER TABLE ONLY prjct.assignee ALTER COLUMN id SET DEFAULT nextval('prjct.assignee_id_seq'::regclass);
 9   ALTER TABLE prjct.assignee ALTER COLUMN id DROP DEFAULT;
       prjct          cnrprod-team-58619    false    221    222    222            �           2604    27878    comments id    DEFAULT     h   ALTER TABLE ONLY prjct.comments ALTER COLUMN id SET DEFAULT nextval('prjct.comments_id_seq'::regclass);
 9   ALTER TABLE prjct.comments ALTER COLUMN id DROP DEFAULT;
       prjct          cnrprod-team-58619    false    218    217    218            �           2604    29073 
   comment id    DEFAULT     h   ALTER TABLE ONLY public.comment ALTER COLUMN id SET DEFAULT nextval('public.comment_id_seq'::regclass);
 9   ALTER TABLE public.comment ALTER COLUMN id DROP DEFAULT;
       public          cnrprod-team-58619    false    233    234    234            �           2604    29024 
   project id    DEFAULT     h   ALTER TABLE ONLY public.project ALTER COLUMN id SET DEFAULT nextval('public.project_id_seq'::regclass);
 9   ALTER TABLE public.project ALTER COLUMN id DROP DEFAULT;
       public          cnrprod-team-58619    false    226    227    227            �           2604    29053    task id    DEFAULT     b   ALTER TABLE ONLY public.task ALTER COLUMN id SET DEFAULT nextval('public.task_id_seq'::regclass);
 6   ALTER TABLE public.task ALTER COLUMN id DROP DEFAULT;
       public          cnrprod-team-58619    false    232    231    232            �           2604    29031    user id    DEFAULT     d   ALTER TABLE ONLY public."user" ALTER COLUMN id SET DEFAULT nextval('public.user_id_seq'::regclass);
 8   ALTER TABLE public."user" ALTER COLUMN id DROP DEFAULT;
       public          cnrprod-team-58619    false    229    228    229            �           2604    28864    user id    DEFAULT     ^   ALTER TABLE ONLY usr."user" ALTER COLUMN id SET DEFAULT nextval('usr.user_id_seq'::regclass);
 5   ALTER TABLE usr."user" ALTER COLUMN id DROP DEFAULT;
       usr          cnrprod-team-58619    false    225    224    225            �          0    27894 	   log_table 
   TABLE DATA           p   COPY lg.log_table (log_id, start_time, end_time, operation_type, additional_info, task_id, user_id) FROM stdin;
    lg          cnrprod-team-58619    false    220   �f       �          0    28205    assignee 
   TABLE DATA           :   COPY prjct.assignee (id, project_id, user_id) FROM stdin;
    prjct          cnrprod-team-58619    false    222   �g       �          0    27875    comments 
   TABLE DATA           M   COPY prjct.comments (id, task_id, user_id, comment, "timestamp") FROM stdin;
    prjct          cnrprod-team-58619    false    218   �g       �          0    29223    projects 
   TABLE DATA           Q   COPY prjct.projects (id, name, description, goals, deadline, status) FROM stdin;
    prjct          cnrprod-team-58619    false    235   �g       �          0    28611    task 
   TABLE DATA           ~   COPY prjct.task (id, date_creation, due_date, status, name, description, assignee_id, parent_task_id, project_id) FROM stdin;
    prjct          cnrprod-team-58619    false    223   �g       �          0    29070    comment 
   TABLE DATA           J   COPY public.comment (id, user_id, task_id, "timestamp", text) FROM stdin;
    public          cnrprod-team-58619    false    234   q�       �          0    29021    project 
   TABLE DATA           3   COPY public.project (id, name, status) FROM stdin;
    public          cnrprod-team-58619    false    227   ��       �          0    29036    project_user_association 
   TABLE DATA           G   COPY public.project_user_association (project_id, user_id) FROM stdin;
    public          cnrprod-team-58619    false    230   ��       �          0    29050    task 
   TABLE DATA           h   COPY public.task (id, parent_id, body, task_name, "timestamp", user_id, project_id, status) FROM stdin;
    public          cnrprod-team-58619    false    232   �       �          0    29028    user 
   TABLE DATA           d   COPY public."user" (id, nickname, email, p_hash, password, cookie, role, register_date) FROM stdin;
    public          cnrprod-team-58619    false    229   ��       �          0    28861    user 
   TABLE DATA           P   COPY usr."user" (id, full_name, email, role, hash_password, cookie) FROM stdin;
    usr          cnrprod-team-58619    false    225   g�       �           0    0    log_table_log_id_seq    SEQUENCE SET     >   SELECT pg_catalog.setval('lg.log_table_log_id_seq', 5, true);
          lg          cnrprod-team-58619    false    219            �           0    0    assignee_id_seq    SEQUENCE SET     =   SELECT pg_catalog.setval('prjct.assignee_id_seq', 1, false);
          prjct          cnrprod-team-58619    false    221            �           0    0    comments_id_seq    SEQUENCE SET     =   SELECT pg_catalog.setval('prjct.comments_id_seq', 1, false);
          prjct          cnrprod-team-58619    false    217            �           0    0    comment_id_seq    SEQUENCE SET     <   SELECT pg_catalog.setval('public.comment_id_seq', 5, true);
          public          cnrprod-team-58619    false    233            �           0    0    project_id_seq    SEQUENCE SET     =   SELECT pg_catalog.setval('public.project_id_seq', 23, true);
          public          cnrprod-team-58619    false    226            �           0    0    task_id_seq    SEQUENCE SET     :   SELECT pg_catalog.setval('public.task_id_seq', 32, true);
          public          cnrprod-team-58619    false    231            �           0    0    user_id_seq    SEQUENCE SET     :   SELECT pg_catalog.setval('public.user_id_seq', 27, true);
          public          cnrprod-team-58619    false    228            �           0    0    user_id_seq    SEQUENCE SET     7   SELECT pg_catalog.setval('usr.user_id_seq', 75, true);
          usr          cnrprod-team-58619    false    224            �           2606    27899    log_table log_table_pkey 
   CONSTRAINT     V   ALTER TABLE ONLY lg.log_table
    ADD CONSTRAINT log_table_pkey PRIMARY KEY (log_id);
 >   ALTER TABLE ONLY lg.log_table DROP CONSTRAINT log_table_pkey;
       lg            cnrprod-team-58619    false    220            �           2606    28210    assignee assignee_pkey 
   CONSTRAINT     S   ALTER TABLE ONLY prjct.assignee
    ADD CONSTRAINT assignee_pkey PRIMARY KEY (id);
 ?   ALTER TABLE ONLY prjct.assignee DROP CONSTRAINT assignee_pkey;
       prjct            cnrprod-team-58619    false    222            �           2606    27882    comments comments_pkey 
   CONSTRAINT     S   ALTER TABLE ONLY prjct.comments
    ADD CONSTRAINT comments_pkey PRIMARY KEY (id);
 ?   ALTER TABLE ONLY prjct.comments DROP CONSTRAINT comments_pkey;
       prjct            cnrprod-team-58619    false    218            
           2606    29229    projects projects_pkey 
   CONSTRAINT     S   ALTER TABLE ONLY prjct.projects
    ADD CONSTRAINT projects_pkey PRIMARY KEY (id);
 ?   ALTER TABLE ONLY prjct.projects DROP CONSTRAINT projects_pkey;
       prjct            cnrprod-team-58619    false    235                       2606    29077    comment comment_pkey 
   CONSTRAINT     R   ALTER TABLE ONLY public.comment
    ADD CONSTRAINT comment_pkey PRIMARY KEY (id);
 >   ALTER TABLE ONLY public.comment DROP CONSTRAINT comment_pkey;
       public            cnrprod-team-58619    false    234            �           2606    29026    project project_pkey 
   CONSTRAINT     R   ALTER TABLE ONLY public.project
    ADD CONSTRAINT project_pkey PRIMARY KEY (id);
 >   ALTER TABLE ONLY public.project DROP CONSTRAINT project_pkey;
       public            cnrprod-team-58619    false    227                       2606    29057    task task_pkey 
   CONSTRAINT     L   ALTER TABLE ONLY public.task
    ADD CONSTRAINT task_pkey PRIMARY KEY (id);
 8   ALTER TABLE ONLY public.task DROP CONSTRAINT task_pkey;
       public            cnrprod-team-58619    false    232                       2606    29033    user user_pkey 
   CONSTRAINT     N   ALTER TABLE ONLY public."user"
    ADD CONSTRAINT user_pkey PRIMARY KEY (id);
 :   ALTER TABLE ONLY public."user" DROP CONSTRAINT user_pkey;
       public            cnrprod-team-58619    false    229            �           2606    28868    user user_pkey 
   CONSTRAINT     K   ALTER TABLE ONLY usr."user"
    ADD CONSTRAINT user_pkey PRIMARY KEY (id);
 7   ALTER TABLE ONLY usr."user" DROP CONSTRAINT user_pkey;
       usr            cnrprod-team-58619    false    225                       1259    29068    ix_task_parent_id    INDEX     G   CREATE INDEX ix_task_parent_id ON public.task USING btree (parent_id);
 %   DROP INDEX public.ix_task_parent_id;
       public            cnrprod-team-58619    false    232                        1259    29034    ix_user_email    INDEX     H   CREATE UNIQUE INDEX ix_user_email ON public."user" USING btree (email);
 !   DROP INDEX public.ix_user_email;
       public            cnrprod-team-58619    false    229                       1259    29035    ix_user_nickname    INDEX     N   CREATE UNIQUE INDEX ix_user_nickname ON public."user" USING btree (nickname);
 $   DROP INDEX public.ix_user_nickname;
       public            cnrprod-team-58619    false    229                       2606    29083    comment comment_task_id_fkey    FK CONSTRAINT     �   ALTER TABLE ONLY public.comment
    ADD CONSTRAINT comment_task_id_fkey FOREIGN KEY (task_id) REFERENCES public.task(id) ON DELETE CASCADE;
 F   ALTER TABLE ONLY public.comment DROP CONSTRAINT comment_task_id_fkey;
       public          cnrprod-team-58619    false    234    3846    232                       2606    29078    comment comment_user_id_fkey    FK CONSTRAINT     �   ALTER TABLE ONLY public.comment
    ADD CONSTRAINT comment_user_id_fkey FOREIGN KEY (user_id) REFERENCES public."user"(id) ON DELETE CASCADE;
 F   ALTER TABLE ONLY public.comment DROP CONSTRAINT comment_user_id_fkey;
       public          cnrprod-team-58619    false    3843    229    234                       2606    29039 A   project_user_association project_user_association_project_id_fkey    FK CONSTRAINT     �   ALTER TABLE ONLY public.project_user_association
    ADD CONSTRAINT project_user_association_project_id_fkey FOREIGN KEY (project_id) REFERENCES public.project(id) ON DELETE CASCADE;
 k   ALTER TABLE ONLY public.project_user_association DROP CONSTRAINT project_user_association_project_id_fkey;
       public          cnrprod-team-58619    false    3839    227    230                       2606    29044 >   project_user_association project_user_association_user_id_fkey    FK CONSTRAINT     �   ALTER TABLE ONLY public.project_user_association
    ADD CONSTRAINT project_user_association_user_id_fkey FOREIGN KEY (user_id) REFERENCES public."user"(id) ON DELETE CASCADE;
 h   ALTER TABLE ONLY public.project_user_association DROP CONSTRAINT project_user_association_user_id_fkey;
       public          cnrprod-team-58619    false    229    3843    230                       2606    29063    task task_project_id_fkey    FK CONSTRAINT     �   ALTER TABLE ONLY public.task
    ADD CONSTRAINT task_project_id_fkey FOREIGN KEY (project_id) REFERENCES public.project(id) ON DELETE CASCADE;
 C   ALTER TABLE ONLY public.task DROP CONSTRAINT task_project_id_fkey;
       public          cnrprod-team-58619    false    232    227    3839                       2606    29058    task task_user_id_fkey    FK CONSTRAINT     �   ALTER TABLE ONLY public.task
    ADD CONSTRAINT task_user_id_fkey FOREIGN KEY (user_id) REFERENCES public."user"(id) ON DELETE CASCADE;
 @   ALTER TABLE ONLY public.task DROP CONSTRAINT task_user_id_fkey;
       public          cnrprod-team-58619    false    3843    232    229            /           826    16583    DEFAULT PRIVILEGES FOR TABLES    DEFAULT ACL     �   ALTER DEFAULT PRIVILEGES FOR ROLE postgres IN SCHEMA public GRANT SELECT,INSERT,DELETE,UPDATE ON TABLES  TO "cnrprod-team-58619" WITH GRANT OPTION;
          public          postgres    false            �   �   x���1�0�99E.P'NjrNP	Z$���$p~���u��`?���V�+$���3#�Es��1�,%�Numn�5�C�N�M��+��Kz	�v�Y�=X���?�,Ql3�����j���ӊ���2�ֿݗM�t��6��3��s ��;�#�Ҁ��v���      �      x������ � �      �      x������ � �      �      x������ � �      �      x���ys[ו/�7�)N3u;�BB�`n��FGm�R$���/	���6E��C��K$��}[��~q��)ν��^�WDX�U�|��$o�a��>$D;�����$�����~�*�\9�ʆ�p>,�� �U��j��U�Cu�X-���Ta*�d�?݉�q/�6G���Z��.Ճx;�����zk��<���A�[�w���ø��z��P����H�s[��^<���?���us?�m��U��~ �Qw���x�~����f�^ч��ꗃx8�m�{� ��m�[�7��U���^�����������@����������à�L��U�Q������ſ�����z���1��w���=l��]l�~[�*X_[�u�z��p����^_i��[��Sow��Kg/U�-?=��4U�d���ũ�3�r.�ً���� 
��b5[�k��\��j��rjFv���Wv��\�,�Q��j�F���5N��}�5��T���u��sG��&/�.�:�%L	=v�ۂ�Z��[?}a�R(O��g��{&����0;f�R��\5
��r���r�����A�jp���Z}u��FW�0������r�[�;�	`��\���*��F��+�+4�Q�FU�`�>��l�&�J0�gn՗^�Z���ү`���2T�`OB� �a���]Qը��.�ݸ�}��hK��� �f�_�8o�O��G0H�V5����{0y���V�]كl��~�Q�H}���Q��l���ۺ��8�ؼ��x�I\A���'�|?
����A�h�/l�ͭ���>�k�n�vO�v��h�f~��ꆾj5l~��.�5������ww@����\]��Z?P����٦O?"L�O��su��Ё9�/�)��.���R�������5+a����3U	sS�b6����Y@D�|���j�\ՂD]���P�U�y�l_�tA{�s��`1�p׽��|�+�����V�  �����xW�F�n���3�X��9�&:x`N���2z$�́.<R�R� ��K������o�N�X�S�/�>5=}�v��d����+���bhg$�@dg�jRX��C�3�3���iѿ��O��'q�/��¨l�j�>�����=��b�yo��	��j�P��u}��6�2�mE�8�^��1�Z�6Fe��8�m(�
_m�R��n�7�����<n��I:��9j � �V��}����y�7�Q�jl� 節��#n�7��`���}�>vi#�ކ��LQ��
��y�b�,|��n%P����
�G4�1/�!*:�4��ѻ�!��K�+C�Фrm��<�$��Ef�q�)�8��K����?��:�?Q+����@�>�E+��Cs��Y��%~�ګ��G�9��%K�{I=x��H9��JC�x�j�F����p� b�X!57|�ew��2"
�B�RIJ�Q.�|Γئk�h*Q��V
�<�zJ+��z1��Cj���R׫��Y�{��`9�Hg��a������*+�+[8�H�׋���^�ٴ��7���h3>i7�ma�'μ�.n,{�C�JB�ӍwP��Sk��%q7���`�m]R�X��3�;��v�E��o�!FN�Gw��]�p��ۅmׅFQ���*�u�K�`�T{�6���i�.�a�o7㶚&���FlJ�]h�l�y�.5��Lژ.�E!�3���N(��#�.=*��n�;Kft7�X�����،��4�����l@N�@�0R��pn�駾�w�^[~+��la�7��Z�ݸ�Z_�5�'�6M�Qp��p��z�S4�TyQ�.�G?+��Ɯ�0����EI��6��S(����R�9e�����u��|�����@��[Jk{�T���qx	ێ��4��z��tkN�|����ks��o�WV��-mm�gb'·���MGן
�,�
�n� k������-�M��$JNTig�acu����{c�c��cq.X���,
mD�A��3�2����oNW��F����i���wy�<=�$��Ix1n5���Z����/�n7�W;��<T�������͸�6P�v=M�&�Q��D�L������s�5�h��wH#�׵��]�2I��u}Z2mJ�������s��m��-i��q����L��7��0�範���6Л�C˅�Hr�UII~������ķ��W��oz����Ҙn��l��/7Z����r����9�~gz��6��P.�QT(d�G|�Yi�
�[�:����S����U~o��p�ҕs����Z �UXs�|Xʖ��N-�Y\���Sg�߻�򥋧��g�P��W^:U
�������Bx�j�w��p�Լ���ū�ϿP	�|wT��k��^y��+/��Wx��/D%�
�l�/�;�k˕\�R������Q%ʪ���aX:{�9��z�F��\,������l��t���/�/��7��BT����e��`�?~Γ'���c����i�U���8}�˒���S�5^(�b��{_���io��n���u��%��%~h����Si?�^k5j�W���f��w&���Z7�n*�)'o��������z{��t�~����_��G2�Ҹ���[����[�엮��>�9ܫ����!�)'�tc����0��RΖ��̔_���Ѽ}���.>��_����,��ݻp���6�����9�gi��]��L�rh��4-�sr���AA�����"Ȗ[��m���7��7��QW�����^�*�L�}�S{̕�Cz{�ٲ��Y��('�Þ��#7�T�d�ɟǷE.%S����^��0��ԡ\H��ܢ��u�]�y[M��A|G6���&�{@OZPGYv	>QVb8SʧIԧ��o���	3��`;��B���a�pKK�&Kۣ{jt�mj-���
�>A������#��0���Z�2�Ҫ���4������s|x8�W�����d��v�gё�b���(l�,Q,؜xQ�n!���s�N�Dg �ɺ=�!0����{�������;�=]6�Wo�L�+�������|V�ݥj6��m(�c�aN���-q���'4�.	͠�k1a�����P���ٵ�* R���a��'���)h���p�%�����l�g�����Z�e6���mi��yu�]��bϸ�&���Ss�6d����Z#g���Q�p6a}$G�& �HI��58r%�@_l�ei���_'��ؙG���{̠�}�(�\���g���p����c��0O<`�j6�b���\B���m�_�ʜ���\z�yG1.���={z�x�ঊ��јwdP4�wԒ���Q� E|K�x���F�x�=2gܧ�=Ov�U��� W���|�T�Q��� ����d�z7�Va��5�����ih��n����%e�/..�c�o��x���H7�V�&M��{;o����ߦ����G�0��{�Q����N�?���$������dc�i1�ҵ�Rͯq�w���'x�s�s��E8+�I�u�c91�>�pn�������X�Iw���e!v�3�*�p!;����&�0c��� VG6&��<S}�yV����I�m��}��J�Ly�n%������N��O�9t[{��|"ި ��L��1���Jl{���P������V���a&1O���7�ή4�]�uyƂ1���ܨ�|T�X`��,��"6��Wnhm�vcU��Sʥ��)f�'C�L�¯�N%�Mynx!�t�������0�dT��-TsE�es�oͩ��4����!�ѐ0�|���8��B�1c�o�>q��b{)�A� 8ŀ�3�A2�� y�h��yD���m�:f�t�p.�y1pl�V�wA�������ҭ���Fm1�4�,����=�K7l��M�"�@ˠEos���c(F{����h�lh���)��yH�g�^5 E�=5eJ���H��!Ѕ9    I�e�2*:L�m�͑���Ҿd`��Ix�1s����ޣmNM;@���Ip.�Â�3�/�����f��'��v�,�{Cqg��3�L?; ƎQb"���i�ڒ�?y�ۈ������T�}��C�nb���������g*���F��c�DO��4�E��%���qlt����}ayvO����=�xZ��: K?e�ղ*�õ7aՃ�]{3��1;�*Q�װ��|��\��d�����U�(���K�W�@��_��MitV�$3nô��'���c�ܝ" �u�4䎇C�`+��]}�I�����%|e��0�xV�p���vD7�G�?4�Z!罾������yeA�nt�k_��E����g�|1�.\[ؔ\͌"MqjS(�t�=MI�*�mέ5���� ��3�p�\1�Ӹ
ﶞ��jq�B|��1c$D�A;(!��\�B^V@@}Nx
�}:3��-"�aX�c��L603@�-�\�CN�Mħ�C�1�sov�j�x��/��d��Vi�@@Ҷ־Xb���d��9NT8��%�&�:���zi �]WF�M�Xh
�q��� /�Չ�؁�N��}x9��]���]t(���Q;�pT�I��7#��k�ϓL�gp�R����,�p��̡Ae|.N�>!���e�@�;�oNf���� r���s/�36�ȴw��@� p��&��٫�NL<�lv��+;'����Axe�՗:A�z-�X���56>���p-�i,�V����rs��P��K�z�S_�?�ޙ�A�������M�t�+eO����Z�k�a�>m��fc��]�4W�5���r�,|����c�k5z6C���w��oܪ���LZ�������j�}��}?��.�������+�|�S묃o�����㲽�j������G�ڐ�I�N���E�O�}q"8a�E�E��������<��/{���'�f8�W+Rs@�����7I�&쏾礿R5`_��{��g��σW"�*��X���w�fQ�}�ZU{�s��3�`����M$	��8�yV�&��&��p�!t�iTо%����81��[k5o4: ��_mp����� 礟,=�XQ�M!��$,�ޣ�hC���sR0i�X/�t�H�-����g��(W�����a5[TʶЪ�j�4��C�}N6ݥ�Mg�#g�� ���Lş��.��ħ��	?��6��_4H�p��2U�7P���Nn�"��(��R͗�����a5_�,KXD� Ns�a���]2�w{��d���J�mpxt�Ɣ��C�Η�@C$� �� *�/�}��vz`��&���ڬNPs�SFIߦ�)�+2��u�(~_P;�Z�7��<���Ԕh��x@s�|u�Һͻ1��������ђAPz�;a�x�����-�f*�4��R�g�~%�F���X`"�dyeӂO4=��N�r�O��OS��Cm��l9}��X ��D�%k���<`��/h��p�=�m�����d�$�>������Q,��q@��-�"0�S0X�h�vy�H�φ ��FJ9c;���-�Z��P|����  Wc�&��">!&P�励Y�ɾ�Q�I�#�i�kϡ#�d�������gRǬ����H����L����lsp����8+����V�YB|�X�����y�'PzhӦ����B��,IdQX.N�D�a*YT�L*�Y"�KJVWɃ�R(�������=��:Uh��J��-�;3��%��"����ͅ�������Q��C	����w-aG�1�m�×����T7?3Z�I��-� 9V��~J�7n-��&��S�@���˄^�.�MJ�M��ތ�e83�N�������w��H^~������ن~��
?�bZ�&�^�J'5GX'����Ŗ�y'H�1��/7��Q�կ�9�lZID�����sO�\� ��9:Fj�#�C��L42�� S*0_��>�[=q"8sKɼ�\p������oC�9�!q������A��@����N0�J׋w3b�u�<�g��}��M"�@��h[9�JI b��9���c�̞3~��h;�g3�	�~����I�tb�M�J�>�T��f�>e�C�>���Zwppw��a S��?N�ch�*����%���:�E�/wyKIQ��]��D� �q����8B�l4�0���2�g�-���V��C��	X��F,����5{�� 9�L��ج�� ��e�N�5����*�y1�l|���.v�1n���g����m��N�yҼɿ���-
@�E�ktg+1�ތH@�C� \w�Ǝ�/5	�_��ՙ�������Zsm~}m�Ӣ?;��j{�ѩ�y�pc}ui��������	4t�/���Qp۪/�:�W��ZG�~5e��7��UK��VmڳH�������qn�Nb��6.Y��@��|�4��iRϟ&��N��J	�zr��⼞""�М0Y3y$O+��y�2`6�d�=���/���R�5�40�I#�K�Ud~c�d6K>��"�FA�T��
L�� �af��+�QЂ�a��b�f��OzM*B�4=��uΉL��X]��R�*��zi�)�#���U��c��cI9dF�u��r�xO�������`�c>��3�sr��KK��-R�N��	������A����!��i� I#<���$G��"������D�\���{h�ݶL�t��Y��ꁶJ�:����,Ikz�evӠ�t��_z�h��N��!�w��NpC�:��ZO���4XRW���?��{vP�J�z(�E>4l��.v}V��X�ԝ@8:ԥv������r]���٥��b�����yT�/��1
����\���`yh�������W��4>>�?f��2��9]1���.$����W2�Qs"c��2�d�6X"xq"����"�Z�LBx��G���2q�	�XaD 8�Ԏ�#�_ɿ;����W0�_ğ�M�o〔�ڱ��wD#q��-8p�.�Ʃ�z�N��B3̒�%��x�fqIyb�Q�h��iY�Ɍt�i.���q_�r9���L�U�+;��!H:�q�rCBEH�jА>@�g���!��=�v�vm����FDd����� ���ir���|K0=���#I�-�8D��F^�3�z��(���&
��bC
8b��0���H<�� ?�\���s� �TE��4�?ʷ��]p���/_�<q������2�/#Uյ�:�VN7k����/_;�Ӆ��-D�fO�@�e�:@h���W�\��Z�Mx��Vsy}�C�0�WO!��G/����w��&_�ȷ�+pW&����ɴ/����hBf�$����ª2�����i%�a0��J�s��޹��`�څ�/^I�۵��s���'��p<��l����Ó�}������������c.xu8]9��s�g/�x��	L�Y�-�Z)�Z�$�% �6�(PB0V��� M��O]3~�D�3��>2�I��S�d��F�� �7�y���Fb\�:�2�@��NoV�]���T�a1���P�W��f�2,T>	���i6�Y����ӯ��m���5�{��ߩ#��)����c��}�v��QϰJ�=�nf͚�8L�M�f�E�neߨ֍�6��ixRS:�6�<�}ul��@���[���(t`�9�������b�cቛ���MU)厍�8:�E$Lg�M%���1�o��LO	�& `r��_;Z�G)��ɼo��O�1;�s^���(�DsԻ�1fЦ�k�	���/Z>n����-U�j�c���e��	Y�<�������}�D�f�������4H(�B��AH�!͇՟��5�ˠ *N�#�={�o>�t��I�x�O{��4�q�>Evp����yan��\�dK�w$�H���;�Q��H��i(md��Bl!��tSi��)4��@���f���3c_�0���tC �Dc�3�_�K��.@r�)|����4:n)���a,&�q�#���-G<� Xj.���^o��1�W&rǜ�K�Cd�bp���ѰBd�L�|P=P���ڊ�    �H�!��uAP��cS��{Ka���U�G�CGCKfͺ�2#��Y5g�P3�R���DK�s�尜�XE�͇X�Q�VLd���r�j��&����{Wp%ؘ��uֹ���v�i�q}#��=�e��J�OR�B�],�A��x��k60���"��w/`��8��0P�Hݣ�/�خy�W\OlCL�D�S�=� ,b�����'���73�����)�%x=����MU^ ��F�~��*����,�Ĵ��|�3���f�v��V"��:���<l�������F}ey�z�a���fs��X;�[����I�#Ѩ9� ��fP�aM��
'{�ڕS/^=������[���M�2��&�`��ŗV�����z�������k�W�o6V�]��u1\�䇇��:g:�9o����!���p0���TFq�=�1�񀘤Wg�^nn_�9R!3JԴ.�c;��C����Giv���s8�҄���莝�o$ڎl�$�K��]K�Bk���i��K�S�F��r���@e��)*"���O�K��N*ȃ�INq�����&����haDΝ2�5�r('�x$�/��[dE��yCF��.����z1U�tS�F�<� Ej�Y�X��r.��Y�Z��"UϠ��T2q17���8�'�dI ��n0*��B^6���<�M��*�vt���K@CG�̔m�W�cr��,�>#e�n���e{���_	�}��d��j>L�	z@��D)O��#�SX,��QF�FlMٲ�K YR�ZH� � ���/7�[��qU��	=V�u��#BC܏�CP;6�v	�j�l��+M�78yM0!5���d���_��u,�s�9�48����Ñi�'��:Y���B�}?���ԮD}�ޣ���/�z͞8��_��g�<��r��r�P(ٳ2B�vT�=e"��<UN�ß��A��-(��ͩ�ŉG��q�`�A�t�s�asS[e���.�j�T?;*j{?H�dEn���V��9Y�,-jG-���4��C�mS��4���uH/���<�?��i0Ōp�r�<�Y��]����堆;8�"*�K��[�Ki���'�r�5r��	t1��%�;�ۇ���,��g�G.�6���!����tF�eM��V$s˫o!��&*yJl�>k���˶� v��95e��S^�g��=�1�$�Q����~-ɹ��Dkm��l�Vl��L3�O��!oMjLEɋ\6�-��}�N���@3	3��>b�����yHT�S	� �Z�=t���3W.�x^&�6|���&/H�,鸥�Wz󲋭���|a(�fP2l�0�g���7f�X�T�hJk������>n�M'{��	�ԄxjB�M��EQXA2�J6�����ȥt"��!> 3k"`d9u����8>ir�y�GV�O]��r�\�R���V?��4�測��ǐ�ۓ�)���x�Zp���� ��Cܒ����!��m-�c&�ܣ8!/�Gv����|2�L`��*a������/"�.\��,,����p�ܕ˺|��xx�P����a�0xvL�U*�n�-��>����1Y2�`��f ���P~�-�'�h�M��>Y4�
�T��4$,��Rn��n��L���&�����12=''�1\�yCI�u"��ѱz��^�W��G�o��f;������MIG5�f�j�"��N˪� |���F�~�����pN �h�q7�Ō��M&ۘJ�k(��򇲤/h`4q�;tPxG(��RPǍ#Ï׻9M�#نL�a�G�԰K#a38F��{���,��>ʊmt��Ye�L4��IB���`g� �S���j�O�(�	'J9�h�-����͑��z�Zp�Q��r���S�[��Z�l�mH$�$�mF��?H<۝���I�����N���U�ښe�i�N6���$��:�7�-���N�&2�A�v?��n�z�"�q/m�Q�-Gy+�,x1�FX|5����x��р����MI��`�<�҄�D!R���v��0��o�Dn�Ú4�JN+����=����8�J�G���i/n�"qi�߳���GZ���
Q�KL7��#�S�O��7�i��gx�a�j��lr1U��:j._�[da��&/���*�*��r���/��ǒ-�>r����J����*����:�u�;��m��5�m �"͂�U�����������!�]���VHNҞ��RJ�.q����?��Bg� ��8MrU1���8�Ц$�;�}��T��=�F'�>�
�%�L*���pYi��.�)\%կE)���T�'�(M�g��t��B���F"S�N.[�,�7B�CeG�{XB$�lISMO�'2��|1ĂDHBY�&�b����l!Pܬ`K�Jӿ`�Y8� S�E��/<�Y;���e�� *��A�l�U�B����$�r1ڦ;��?���d*I�v'CCr�i-�򀄌mѝ�
3�܆M�����h=�8N@����J�I�0��Ŧ��P[:H�N���������{�U�RG$
�;-�Y�̼{�w5�̔�[R�A0�k�1�Ǔ�F��\��=K餃�i�XA�����FgE���!j�Ӗ8��j�&>NpFL64>�] �e:D�h0��@�EX͑�}���[(dR��cg�ZcE�l�6��ѻ9����耹;`��8����<���E5�[��Q��6��2����b%+i�-�J����|Q�VԪ<H8c��w�.�d���Yb��p���֭�Ҽh;6���@�tƤ�y�F�`X�9rȖ�
~���kzq�� A$y���_�J/���d��ue� �4��V���U�� Aje��<��E)�/��[A5�:�pH�u��L_���d4^!Kސd	�g�נh{N*Z�Fׅ��N���\��I�����e2n_q�s��=%z\��!��/$x�����]V�ld����<|`�ר�7��Mh�,�df�yiz܆:]�"�W$$�y��pj����I���e�ҽ�Sd��t������s�L�4��-��i��$]�{��"�����NhT��\�;������a�Z��
s����E<���'�R0��Yb���ʻ�69�ζє.g�f�GKfN���d�R�c�������Cm��H�8�
	�ɩ2��I^�
 x�-PJΈ��'�:Ѥ����S�[�"M ���&����C]�`EYK'&�Z~n�����5����̥��#G�ö���¢��Mل��պr�[<��i����;��=H�{�׃�����$�C�{3��'�a�S:L����{@ez;�ǫ̓S��Ŧ(��s7,ir⒞QA����ƍ�Z�p���=��6UL�rL���E��Q�{�k�BѼqw�
$�Qω`r���V��V9���S�˓`(�����|�b`��d*�٢�F�<��t<y���[�	�y��Kϟ<w��9�_���2>2a.� ��82���E�p5��?F)M�<�kD�@n9n6���7�Q�����@,�זk�:�ђ��Z�%%5V�o�h���E7�0g��lDL=|�qs��t�~�N��*�1-�B���ڸ��>�\�\���^�gIؗ��u����tQx3]+)+�T�|5W-�@�R�qO_D����R���k��x�� ��X��D�|�����8l�o�Rᤵ�YUOQ�OQ�OQ�ߑ�҆&����d3]T���r� b�k| ��@m�0I���g�)����T����b��)�e��2�<fS�Jzg��[�l�0�.6nl'D�Q�ӪS��I�7=��|1Y��g�M	ퟆ�=|��Hc/���M�� j<k��ڌ_㉲����g@N�\��E������$96o#���8ᶑ��-����G��V�V��TPi�$
�Y,+Yy�X�',-��K�n�,���?�.i���}�}���W
w,9�\����"��E��z���ڧf̉GeA��T�|�naȮ�eC�3Վ�=sN�%�wtdp� Ek['n�H��{�pfQ+\��@�{�~�i��f��$-���(�����i��p/�    Jg4e�ՐcLd���]�kc��/�*%�� ���1 �_�f+�!��B\
�/(N
{��վr��5�f��ϗMq��!\mS	q|H��Ҫ�΂��s��J��ռ%Sx���C�R$Jk�Y�#�I0N��'_ϝl�B1����Z[�-+'������X$��;��M �{L<C���%J�^����gv�=	��%Ia}�y�<7�IF��������S�~%�%4N��A>q>~�D��tR���z�����J��Z��>y�D+��ĆWB�ĉF{AG�Ko-,ݪ5V�%uy�y���Vk�ĉ��G�S�ܬw8���	V�DT�%���y�%�F�%���(0ʤ0��&\� ޕ�0�"���] �:��q~m��d�_L�81���*.�)5�0�P��|y��j`0���=�?l����.!���7j+��.A��hy���'D��k�B���	���?�0�3)�d�d܆r��������>ܮ���V�0u9�3��(��R�es&9�5ᥬ/䱾i��B]�>'��|7���!I<FF�c���L�����Z��J1B~�J�b齱�C��@�KXh��F��k�N�9��pB�I�.];E]3QF��eLeA)��Y�Օ��k��f�xg���Lvĳ��A�!�87��ݛ���d�`;	x��ڬC<k(�4K�S��ZHi:JZq=%i���,�44�"�[�u%I���e�5[J��`�H���;��z/\'��Kk��P<���%#�Ԧ�y���1�1�Z�����E�sX&t��Q߮M4Wm����.aW��@�9b� �^�&bn��OH��Jads	" q���02p��\��7�
��1ʘ�H��F�Ɏ�1��x	@��n
t�����s⤀��ׁ@�IۃS,8�CQX,�X��X�,�4*����܅Gɖ������g}$���+�_�ݮ��Ǝ��E��!T;��HӁ��a)%SiW�0�m�[����l�&"eC�"S�f�)�	"e��L����{�>����S+4�`�:�)�z8��}F�,���J��j���O�UA3�iq�:���f
-{�{������6��W�J��Ӕ�'�B{)s�N�+�6e.*�~U(V�6�	JU���5���.햐y2�`J@�7DR}u�L���5޵*�cY%����*+	4��q=�_-��lk���d�h{�)��>��\�̃�ⷨ�[��Z㵺1��0�t�5(�=;�؋NS�9��UN~��W�l��
�Pb�E�D�D�TG��Ǚ�9�����ښ��9I8{d}`�1I\0�Ī�����H��+ahOM*C5���QrbVi�nov�C�)�Ø����$re�pk+_K��� �I��<B��Pnj(��^��c[:e&&�`�ve ����B�1�\���$��'�� w���`,�#V��&�1�d�l�L�Ę�����|���4u�i��_V)k�](	;'��I� �]��b�؟�]W�4U�����u�"˱vV�Ƃ@�N�$�W>:8̅�Б�ޗ���N�`
�}&9�{��\�����ѻ����+��qzo���R����*���Y�ܷpc��>P���
m1�,T�P}j������\�3^ߨ�V��ҟ)�͇��3؞������.�����+�c�Q��7k��'���6Y\���t��7V:��z�j��N�L��?�������*`�V��S+A8-��gƓf��E\���
2�F�Bd���Uה^f�n��ז^��.'��Aѝ2��p�h� W��J�Ċ�
Сey�R�^��﫽�0��O�$��-�@�4�޷�%��':xaSa1`�p�n�_��۾�x�~��);plK�64g,�=w��঵���m��Z����hA.N$�6�׺+�/�����!��{�#G�q�S���L�wlSr<TqO���̚DUn�=�B�zw��΃���$�&�rƃ��dVKM���
��0���cN%j혋��-�?i�a�I����f<L�b�lH�r���{�΃��	Y�=�����\F��>弁�,�^�5Vj�W��4�����0X;�+�&Ҷ�/za8�Ӯ�o�@�pj��tw�5>���|��x =����C��B%�(�m_�陃�.�q������J�J7;ǊNyG.� �$x��R_UJ{p���j�� ~�m�C:&]��\S��0�ޛ��==�]A�*z��������W�pf�Lxl9�WFr�dG�{�q+=���k�;с3FH�Y�,�,1*��+�{�8wb�f���S��έf���u,T��>퓤�����\�E��H��s�2Z!��x��m�J�Q���\��Rn�-�$	�q�]�ۭB�7V�o�F)Z���_��i�l#;{��P?��b��6^��d]7sQ�Dr\~)��5N�CB"���{lIm�����Ȥޣ��煤��g��uh�`�!7k\:D���������Õ�����2R�O�Bc��?�B��Yp���͐�͢I���Ʉ� z}�N؍9�r�`Q��l�H���ޔ�7nP�l�V���q�J��\"U�Џ��ip1:���S��jQ2]��i|\(�!�@�34ǗE;`��A��k��i4ɪ�QH���7ӕ	f�h�L
Y�6{���W�Y���IQĐ��T�w>�5ȅ��G�ثcH<��o�^Y3٘�X�Zah�q�
8�@��2IQARY2�E�;.�-x@㌋�������52�C�MtY昆?�^4=�{Ƞ��i]�)T�~��������N�RC�����&Z�	����T)_�bW�|!���wY��K�rG�8������K��<t+p��{E�G���@"`�"���.�f�%����J�7V���}e��֠�VGz�|�m� �ish"�6MmL}ʢ�*�H�I��MB�>b�� �d��
#�w��a�U_�u����M�%5h5�;����f�:�d�������	+��"�~�A^;�#4�8�@U���3�]9�ݴ��2s�	�p�o�����&`{���[�a�|����</�}�qE��&ܕ>h?:\)��� �.}t(3����4��g������׃��0�$l�q�*���O��Uq3ǪM�:z�"� ��5l�g�\D�)�&
/*���b(��&0"�30XB����F$[���pkN�{B!�)?�!�E쓲Yk��ܣ�zݼn���� ���%q�n�1�c�c�֧-�՗r0��s�?�b��Z�q��N��*��4�/���	��^�XL�[�sd��D_�d�+ZwY���߬+c�T���X���v�F6QM��Ր�KL�it�4�D=s���l��$qf�wc��F����@�l�h+��X�(����ѮPF�Xy�w�iKR�\p^_�]����u���)��Q_��-���ƍӺ닧^�p��ً^���t��/>W=�S/>w�좹���,�$j3�!/��y�/��[�^�T-��A㗐R9Z�_�#ϗ��3���AF�1��d#;%���ђ����$�� 7�3�|�c�.m�^]���p[%1��\��.��%1������AE5xW�B}�9#��x�A i�B�ux�n�����e�IArN�m@�:��E���iA��06�3=��8�U.b�w�y���v�t��t���u�۪6���ǩ��=�M�?��#�ꓞv��R����h�Nk��]�"�V�~���@z����N�$��Y�X@�\�9+�Wb�����4��2t�ÿD�cjc����Ӫ�#��f8�'䁴ʭ�8��r<}�p�^�ߔ^��0���ʡ:AFv9�_,��4�́�V��1��a�c)G$��P'5��$Cc��	�������.��/�t�`�һ�s}�����kG}��ݮ-��ۓ|9]��`MWCh.��	�`����A��u��&�z������hzl��3(i�%~��kՈ[o�l�����8�0f Cz��x�<\k��!�:ћtZ���ّ�?fڝZ�� d}���    z��g���3���v��f~G������l\���{��;h��V�`�Sj�G�'$�/1��r8Yq�1����ƅn�y�����/��2q��8H�x�S��U_n����}��y�p��'~x�g~4;I�+WJ�@)��B>�b���ޑ�BK�/��6U�#��h¤���ȅ��R��H7-4ҽ��u-�?O�
$��"���L�\!�z	��LU�'��%&�e�P��I�ܪ#�-L�n�wW����v8��,���,���ۖ��֓� r0s�֪/ܮ�;��Z��TouZ5���7k�e�g!*/Dѩ��,����X���cD￰�	$�^��>�V�+�έ�z��W��3�D�%1�꒰�0��ő��%���QO�
��xz�t���.�6�\Wm	���՞H���P��@���]�t��	,�X0nQ�[c�l I,��vmm6/�H�F
�Hz#��S���J0d�T��:�<~���NO�b$�3QT��OP�(��	�jN\+�@��Z<����jZ�26`����M1F�	�+�g�1v��#�dw�q�7�g!'��]�|�4j�����+��M�!$�k��i`�y��lJ�k@nM}Y];�����k���񤪇��/�s2�x��6w��Z��V��[�6-k�r]�֘R'0x{��vm�U#mӲ:��$���I�8"���H�Aq9/@vGK���h�֪xp{q\E���X)��J{��O31�M��Ћ��
��Q1�.�N�P��}^,����Q1�"�d�\�:���%�4���Z�	@٬&���Gn�0���Z��#��Bn��-�a����ȖU2������$b��v�\��3�r"gd/۲Es� �I�4ʨ�0B
�<�Ń%�DL��#@7ۣ�-���M�[�_��Zn߼�rG~Ŀ#/:r���n�xB�
6.m���M��m��}�c��%��ڥ����S����	p��7}m�����=?��Z!�_����3�@G�ISg�[_��
�s�>���Q�%'y�h���q�Rp�[��O���V}v�� �?��$�Ř�CR��ί�7���2ŋz�+�Ba ,�,��Qjm�T�4�iQ�bd9Y'<��&�	/J�������;6f
��/ڷJh��9��_x@���c;`�������_[��Ǧ~c� �/ɞ+�契w�z�R���)���}1����q�{�r��&�q�>q��tD� �
�4j����.��E�i������w�+��,!�wQ��I+I��>Z[��w�p#�����:G}o&
\���m<����<�¢w��!n��_��k��ʉLJj�r�O��)�喖_i��sE׎�-�v�̖4�{ä.����)�bƐ��v{NfX�ƙndc���J��/±�+���[�������-I��lZ�L��6Ye�5�u�>O�M�[�өb�щ9�'AJm@:珛p�ilJ9��&;�}��Wܢ_�
c�rԨ5�ScK�E��w���m�N3�$)~�w>qô��,��
�8�f����դ����r�B��MfU�<�c�3y��/�x��L&M�Zj�gʕR��-!s���|�$�@p87���d;�R�����wp�X�� �~����*lGcޏ4��/8cQ@l`Ώ!�,�3��yG���:���C�� {���t�e3��u�c.G��2��cj��E�6(���t�J�R4�#�1�!t J\~v` ��G'�mیJb����rf��G���^э���0>�@wͲ��ol}��f7�"n.+��&9Tȉ*B%�"*��cez�`�?��\F�%�b!�~'��X�nOtq�Ô�.ڢ�`��h$!;���r+4�0H)=9����C��'�Tc^F�.SFM-Éo�~oi�V!��1��<�EJ�w�J��j�g����Ӝ��
�5:��*��1��i"��u�x>t�I��( J�hи�~�`<{��\p��K�0���h[$w��dG�.�l_�$�w��	��TE~���la1N�!Z��r�j�<����0��V��*�Ir��J�K�q>7��4YK��qObcf(���%��}pi	Q���·? E
}OC]+�F�l6�$��I�5���Ҏ�l���%'^�/R�N�����xr��W㚍��pՠO��R��o���Q�%יL�Ծ<�|r���~�Ike������.�����_�?^������^�?������v�*�v���ſ�\�tQ�q�>s���Ǚ���g��T��7g����9���ߢJ}��%�ǩ+/���D�q��ќ~	��t_}���C�^�?���k��������x�E����v�o����]=Mo;��9l�)x��E��?9����h�s��W�A�.�����"t��.⫯����k�꿁�]~9{�v��������V_��CE�s�'0���mW�AC�<�����l�[&�yD�)�S
ȧ����ʖK���0������(��]�<`�*���O�!wF�S=>��=��:5��=�hRs �.������|'ڐ���5iKEm�>���]��]c��� ��a�6Xt�l���:^AJ�m�'|]��N�˲,��kϰ�M�=�:��*�� ��O|�7[җ����o�-�݄�a�	p�wy�]�����"l�s�죟�z<WGw˿�F���� ?��h5ogj��Z��YXj.׃��<��Nӿ�����@�ì8]X�ڳ��d�W�_�0��OXoU5Pͺ^�y�v��y�޸y��"��R��W�i?�Z7E�N��sL�61c�5�9�6�q|�*�=XM��u��-�,�����,��Z�ը� �[���)ѕz�L���l@��,n/?��H�j�������ֽ�H�O:|� �[e��:�o�����F����w��������͂1-J����T���
:���A1�-U}sPzY:T�c.�p1�o�S�cGU��,����T���TQ� &�B�X��` �|[�?�e�xB�݈$4���A�����h��Iq8lZ%�$�j�8=\4��������[���3����?�-�ZX��~x���b�J�HH�h�:�N���6��1�q�>�|
��&#��g�Cw���~P���H���!XS�P}���]��~��
�0�H�0�γ�Q�
��1LʵV�%�<���jA9�@��m-�Y ��0�J�-*�P���ZT@�^�!�;Zx�~�՟�>�*�6�KN똶���?���J������\UB���ĽK>�q{U�|���I3� d�$�C0:�BNM��<��� ]��7,�-c'���;D����y����O%���Tg,o�v	���y �aJ�A/�mS
����0e/�a*�(�X��3n��ۉ������/��J��`b˰H�4B����<�i���iܯt���e5��������x!>����E�����"щT���6���y�Ƃ+h�ue6n�f"�FZ���3��^�c`��@��N����睏��/�m�S�h"��Ș�����hސ5r��6y[��S�G��!�o�Y��׼o�0"}K�`��˭3h� �j�m�L�]�S��6ʽ�`��z��m��$M���~�ܬw�[s���Ls*�tм����L˥v�"���MaV���=����4�J��mDw��_5h��צ�z�$�^Ɋ|��Fʎ��G�b�>�p��y�C\�·6��(�1���"��ݱ��(a�K<9��c�p~j�;��h�u|���v��))��j��T�A�����[{0��k+Փ'�K�z}������|T[��(Ֆ��j�r�^�_���?.��W
�lt#Z*,e����써�&3�&+9N!��%��1�.B;����ۜw���� �]�Y��Em�9�z=%����=�C�am8���$R��֛���5w��`�����3S�By�T���G�D��)E ��"0 �D5�V��������xd���?	l+�&/{��kN������Ξ    �Q��5H��� %d���Kw�-ޙ���\��(��.�_�U����3�����B���+����"��-4�(��p�t,��:٥4��q�s���νt�${��]�T@��g-�^@J9NrE?ų����d4���k���7��/#�;n�������
�z���B��V�C�3懥�=Z�u$XU�d���{�%�fm30�ؐh#��=d.��?��Xg�$Z��;}ܩow�^��@,7���N����6s��L~�	Q��7	a���-�^���<V,���l�Y���9y�8j���ߤe@�ގ��e����C��	� �D��8�FH�D�D7�GuCw$9P���I�~/�����N�Z��mrYk��MR�6cD�(�'|[6]A�+���g���j�Σ�!�P��4�^�w�!�d�*����m4��	�l�];Fo�\"�J�w�`�,��5�	w�pM�`frǙǌ�QX��9��]���@�[��X�V�Q1؋Eѵ(�^���̌D�W��) �Sw���ewHKB]'��cbv��MRLbQ����m�����iFΔ:Zt��nkO��u��@���ʡc����������`���1+,�E�?�^l�g�q�@<P30�w�֤�А��;���Zߔӥ�Ȼ>sJ_�0���w�Ձ��G~��)텬k���^�Ahh�b$�*C�ɯ"��x��ȯ�!r�hJ��m����5x��"3��[��cZ�ͪ��������Z�>3�H�o�\������*6��o��%�
r����-٨��c�gs�BE#�M\��~����ξ��K(����(�eR�]Pr���N��˕��a���W�_}�l��T+H�D
c��.T�02�I�:̍�0Ñ-݄6��	s�e+Gt&��糥H/�����Ә�t������\��zg:��,�a_�\2S�rv�T* �A9�/i��2j+7)���l��,�;���ˋ�B� -�3�۷2%�jo�ݱp��X9�:��G:-���0{C��ꝁ�d��f�� 7�Z��xL�je�'�c�H�-k�����gۿC��ǎ�K\��:�?��}�9ќ��bn�eBLݪ��1N*�0��殧��n����O����=x���l"�N!fz�=l�Ɨ�مv��Yo/,ݪ�ެ�~w�$i<�V��Js��P�b��!	�-
\�ꄛ�I5��]
m�2b�Єە`#�؛��Un"B�����K��1�5�d�ˊ�Q�E�����|O�WJ%Fa�.7�����Ł�a��鬬�,�e-�S"*Qi���)�d��}���z7����O,����T�-�F_#Ɯi��՘���a՞.9nȹ�tsU-p"�S?_�E��c�x[���L=Onz!�����	I��.��w��6�xĘ���m�*���	�.M���bA�w�ۧ>���0_���Bd�_���L�,�Ys	������2�f��ڤh���/IƢjÞ�l;�����غ�;�IbS�c�Dw��/���C'��Ȟ�cJF�x����t���N�F�JЦ���s�����Mi�@��M��=u�|Ĝ���~�,&�G�|ԛ�
�\��de��Z��2��n;B)!qVD>��ƨ�?r��uZz0���gn���Uz��E���u(�(/���+l��:F�T&jaמ�^��� �ą��#	�&����$�Q+�gH`,�����H��Gs�?���Q��B*�xW�w79�)��wҋRa���φ9C���j>[�"�Fƻ˗�ĥ	
��b4�!f�~,�)��Y�Z���!�
I�N�1�+R5�R9D��l1k�ڠVI��a����j��jD�:�c��c")�2jB�J5�1�n��RWL�|�V�d/�|���L�%#p��ۿ�����J��ё6y��<��A �.	U�xF�0ՐxFS��w��bE-����n�ЕR��pX(_��9T����Z \�q$����c��m�*�~ ��j�F2 P�أ{P��7`N����F�Aܧ��]׎2�Űr�[����(�
�Ĕr`�2�k�U��yC8�_���q�`�������IU:9��G�9E�L�U�^L�>��r]UA�Q ׽�4Ҝ�e4�+������Gd/�C
��mF����!DW(�2����.Ƒ��D�LX��B���;�Tu�y|f�,0�s���,T.�n%(���L���i;#D'�b�H����*8H�v��!-�̠2�Zc�X]o���Fb��2����s�|��=���J�:���ϕSAG[��yÂG«��~��kx�L��ݱ���Ɵ�=s�|��V�F'8u��\J�H�{W[n�I�Ưu��6�:vMRG�:_-�:؆ ���d��^J? 6(N����z}u���1�4�i"�w==Zz�X��U��j�y��@����2���+���j5�Xx]-U�a�uM��ը��JLI8F�j������e�W���^j�k���B��� =������,�wi��A;�0] �����Ko]��0O���ʪ3E�<�QEv0��$>��i��K9�vy�xyb�D�t	��3�:8M��7[�A)��h�?6ڦ�0*��
sP*��R���V[q>,0��u� �����C�_���蠺�N{}T�u�ԣIn���EFI=d�\�2�A�EM�C�ʷ�����w	��&��׆P2KK�Xԏ]F@D�lI[�y�6 ��+���V��N��R[Mۗ��u�z-�R�#c�EMj�9SR��ǆ��g�M�,R�����O�ؾ�Em��d�2�QX�Dʂ���H ��ih!Q��!
<�Fr��x�!V�s���q{ޭf�SJ���j�Pn�5I�w��tk��7UY���B�������F�[�G�S<���G�e��帉s����6�4C��ZL�Or���h����"p=���5��n�6�ĐKI�p[�� �N.ׯ��<	=���kP%m�f�9�q<C&�܆�_��_['ĥC��h��%c�>�	A�S��0�=9+&sJ4��z���3���b%�cS[����A]愮�}sWD�=2�tW0�S��%�l�X6i�h҇'뛑�NM��M��٪�Ƃ��(	��J.S΀��L6$}�fCb�����L�I�i���{(�t���׬��+�m�隝���\yC2�hr��NnsKm��a����k=�#�@�o\}�m��q��fǦM�F-!�2�jA\3�L�)�D�_A�7��Z�����N+�������Z���X��㔲m�Ǵ�.�]30��C�=3L6��c�򩇱��k�ǝ���._�d�#tArᚣ(e0��;�AP��E}m�Q���9��PX�T	pR��2)'���ƚuC^��Hu�4�q��ᄭZ����=��j0m���l����_����)*M�:K�������\�N�;<��+�I~�Y���H�o�������d}���k����a[�{D(������r@��l$\N�\	
Ǚ�k�_�^}i�jir_>Y.J{�����5�TԽ���C�Ķf�Z}�-��<fU��\���l�}*Ä6}H.������~^"=���r6�L���pb��/b�����h
b���dJ3pz�7�*����{L3���2�����L���ƺ`�86����A_�!p �*�����3�U���Y#��fnҞ�ÒT���?Ri:ݹ�uɧ�1�ɱ#�'����Ώ�Y�����!KQ����vlż�e+��y���<�+�Y�)�M-;'1m���z�.r��iF�~Z�\I
%l�G�g֨� ����aa�3����#C��Gcu��l�o4���2!|�� �1���жt���ڔ���rg�
zѥ=���^���TB���4��Q�R۟�KK����C�;@9P�T*�C��·���	���0��0��0�w2�ԷJ�ż�r.ҕU!ē�PK�`sCB���F�!��x��f��qL�`�R�N�%�~�	��It5h���@�O�A�K�^r Қvq>��;���!$V�L~�	��� R
  ��Oir�&�6��)�OU}�T��{ShB���A�<�d��#A�1m����6�v��Rp��'�C����zŋ�����Z.Ɔ���wyx�R`���L�@��Ѧ���@Y�$���c]Wr'�\�
����B��`t9[�ʕ�>�r��y������"L*cC`cK�^�����-����
Sc4�~H��aS�vƩ%8fϯ4�fN7V���Wo5�W��W�[�����Z9���CN=�^p����0�R&�|������k�,:����&K	>��`�ĕ�?�+鋟�g&ZJ�@��>�G6,1�ͫh��,�J�fP���aN�oѹV�\�r�@��G,��F>��T���{��q�)�f�g1#_-�FcO�?��9��xFmX��cԢ�]h,O�z�pB�}�>8��`r<ىsԒ��۩F�� z<p�R�pF�HڜS7�FJܧ�y5X:n�� D4j��o�qܢ�j4�|��؉��㵮L���k�c:Q��&uT� �nc��E1.*2�&�=~��-�c]��I$&�4e�Q8\A`�MFN�[��~xF�]���Yl�q#��Nw��7f�N�*����g_��^꽟n���L���Z�ϥ�t��_zźU?���V�; ��e
69bDj����O@�"�gQQ.�sE�����":i�I;ɪ����bn���q��@��C�W-�'�%�(�2-��
���@����=�		��hC��5J��Z�.��Ӑ����B3�?��9uH/5;5�v�C��H�OϤn�W 2�LC�=X97����YE&��.(2�I`Y6�;��[����W�-�ĵ�gM&��P	~T�h\���hv�=`<uLA�!Y#Cl��7Q�U�{�����4i�%�I�E���;55|�ˣD�m}��6��#$�<T�|�G\EOx �3f�X��TX����������j* �0_�.�)2tѮ�l�	t�1�+���N>���kM������A;�΀ܨ���Ks��Ip̘�"v�*�"��C��;%��
x��~���XZ�F���Q���e'1O�,ߴ�Wy�T�T*�n�������t�����"C��O!`8}�1ҿf 0+W�X��m�?�\o��Pr�c͒���ح�t��3�q�[�ը�@�I��7��žIJv�7h�',OVsd��d"u-��e��q!rlص^���x�����!�-&+p��M(��ӏ`��Yv`��{K�N6����5�6��d�-ه��v#�1�#0�JTevB%�[�+�c��G�
v��Np
=�8���G5�3�ʺ���y`M�p:Ym��6K�R�����I�Q����dBN���AB�c|�B/�菕O�ۣ�u�9�r���^	�^z�܉�U1��!&H�'Is4E������ƽR[z�!=�.��_�{���1p�ti��[��5��b"�yT� ��k/�j*R��G�'/�Qա}� ��3A��9���z]�,h�
�r�F&�`��"���.�WCH�=��˖F�K��j/��M��H�@	��v��u���=؇�]uE3�2���2̒S�
�~���7#��В�p�i|S�LD�T^��G"J�!e�R�n*u#���t��Ӂ�u�w���q3�_��b⹓ _5��)~&b�m���p��.3��$�Բ��n	�s{r`z�����=ۺ
��ӗ�W�]3B�!Y�G����5H�ymi�lzofd9D^!��r�y��~��햨\)�E���%J���f3e!��TZ.�nփN���Q��.�`8}~Jjr6������-}�E�U��L4�q�Bf��E�&5tlR4��v
dҁ����!M,���aԛƌ:	Ws����@`�}nv�`�6<�O�^z�(�O��B��������sg�������̆�3ｃ��GΜ��l�\?s�9}�(�}�g�5xdW��5���x�&��7f�����UHY9�q�i�C.	c�qA̫����Z��O��(����3V]8�lޟ����W��3�4��G�,$��Y�Hw��� vJY�B�T3C�m�?�����h	!p.�\� �{���{V����c�,����ϵ�@��j�*��#��9�ɼU)��f��`>ְ1�'��9|��v0���>2۰� ��耈�lPĎ}VM���G�A�M	��t�V=
D �8P8b�qz�����GB��cgD���Z"���:j��Fa(H�p��s�P�F0�X���F,�C���ǟ1ph���O�T �Rk�����o��/k=�g�Kha=�2r��=:>ujr��5���JJV��"!b�<V��o+�ۉ�0��&r�Sl��3�W��q2�*��4I_�5s];��K-x��k�$�l����ذ�(@���TϫIr�co)#��F��	��K·��w�_���/�S6��X�u%L�S~$p/���@G�f���d�ö���!Lq�;���`��5��X����B�<�D�#nv����҇�*��We�z$-�]�$����u�oʼ���j>Q�v�pq_'��V#w�x8N�nI�,��H H���Ù�
l��v�P�Q����2�[y)L�����?d�y����>b      �   y   x�u�;�0��S�by?��-=e��DF�R��¢
�r�I��;�Nm]��71y��r}=�Q@~��v'��ڑ(:p؈S6�b�4���e�Zn8~/�B�y<fӐ�|�{9{�8D� i�+3      �   �   x�m�;�0D��Sp���|JJ:@B�BP��EP�p*@�΍HD�F��ާ�>kf�f]�v�0��ܖ��B�!&�i�3������(�!B�ȗ�X�A�4��L�;��������ͽ��{��#l{�^�q�24ҝ
�	v�.�UP���͊})&|Q�
Uq��!D��K�|I�����g�|�      �   &   x�3�4�2�4�2bNc �a��̀��c���� ��H      �   �   x�����0���S��}C��ɋ'�^�1��7������	��kY��1YZo�S�"�y-n��y��/m�8^"�"<��}�ď�d&����'M�\�I`%p�	�G4���s������ڈp*-(9��:ؾ�k��T�\��Jk��U)T�*�~��,�^�-�6G��j�o,f���I���5����	����{����3�'�L��̌1O����      �   f  x������0���S�6�)ړ����=z�Z�,P����P\�w2�@N����3{1�!�l�
�7�������6@��}e�ܞm��"�w�-���7=����ǎ-��+n����������mN���͔f�	b�r+�t�����A�lE�1͛ݨiF�	)�6+��'�����@��J붹���4 a,9�)�)��ui�+�JE��UV��m�+L���G/��y��b\H��T��4���u 5J��KL) ��g6d�TJs`��Ic�i���A�!b��cBAu��)�@'^�&:�R�%Y���o��~�!K��$� �()&Aֽ����h�4@&t�(�?&SG=      �      x��Z�r[Gz���~W��݈�vQ�P�*U�^A� AE�����*UY��L93�ؕ�ȋʞ�2� �Q�> �7)S%.2�����tF�������w��?}4�j���'����?O�O�%G�}��ó|�����_�GD�cI�ec*!�B���yF�H�J���k�\�X��v�
�8>5�$��?�v�p2��}?�n}�A�]m��ש]�c}_-%��2)�b��9[-C*8���A�X�IZ˙�آ��IA��o��7�L�c�3
�هOQ��~4���?N����/$�'������G��߼����ee9]�.Tf�1�s�"�4K�S�%Q�C�If�w�G�S��I"�<x�/�5�L�D��S_v�o�R��kk���$�re���S�� =H�ȒE��E�C��J�K�;]RJs4����֍F�"����2�v�)��W}x�S>�x��(��2Lg��I"Ì��P��A��\ȑi��\r�st��8Aq��$rr�ɇ�M����h���j.���лB!'�y%BQ,�����+��Bd�P��p�,���<C�����}���X��t���}�E�O�d4�#&:�eQ>��ȎQt��̌�{'�,A���L�kl¢���B���g�On6�L��������a����m��|�����Fi<UNk�x�4%o���:nrT�y|�Mph��A�)K,{*��8r�������i�������[�D[�q�������iF+��%*�U<�:%���)#Jm@�}Vkl�>1�=Sd|�|л��a�L��g����l�_�����/�.�����6��䏇�0�����3�[&P~��*^�-��X:�|
�<ȈY`Bǅ��=~�7P�a�L�K~�J�u�#01�V���v bAS%�w:H��+�֞i�-M��yN&��BEr��fe9X��F!�����a���i{��� `�����B�i؎�q��;U�Y�6�H!J���SS���30���h���I�'�mmҊa^�'��/���7LT<�4C�߶�}��b_�V� �x��^���T�ʳ�\�/���u$d���EN�p�# Ɍ7T��t��[�)��l�|�v��a�@���.|7#�ڔ.A����"��Q2 ��\�d�C�C�Muz/y��JA�F�D�$e��v	��I_m=�ۻ}�^�)b.���t�̃��%��J�p�,ʜ�Rt(2(z)q�D�(mE�T�:E�"w�ӣ[���
Ϫ�C[Z���.9;�� ��Q ӝ�D)�9���)�_/=s���q���(\A� ��h|����BQ�@��ߦ�g�4�Ԗ|7��W�z~z9#�|��������
Γ��A6!ƩD�DOyA�3���T�5��� *���/Ƚ���a�������|�B�K���v�<� ���I� ���]���D�(Q'���|
�RW�%p"�2�hbb�F�G$a�f�����0W�]��gpx���0T�����J��F�H���EׅC�`X���!;�V�"Dn��Z������a(����^��%q_ar�݊dПu&A�h-([z�0z���I���(eJ8쑳�����V����ۑ:��gK\1��GK�~��ī�@s����&*XDV0�Np�<z
x`��'O��Yd�Y���&��y{2�>�w��+M�e���-9^VPoZ�^�G�iK�V0gUi;���,3/�W�V�'�Lrg�����Q�Ŋx,D�R:f"�D�H]���cLУ�����N:a";a�щ�<����� ��䭍ۇw⃆�(/媫[U�檵\zppeGkc@��°{I%$)q�
ͧ�(����G���?CE<'O|��қw�%�/ZNz�՜�F �.'��S��p��S%�
H ���ïz����s�6�̽@�@2�{v������?|��3���n�&�hQ��T�\�<�k�6���R�U�V�U1
��1Z
 �T��$E�B��b�`�?i�Y�^�/�7���&�Sмr����!V`,a�Y�Z(�px��2E,�n@DO����m���8��q֌������F4�蒝�Fxä�#�����u� ))��}	�����w����,b���ԸA��O�o�UC�o]sa��� K���r {K��Q�{� <���'�:���S�Th�>�L�����S���y���h�d���2�+�����D�b�� N�����3x����PV�D��U��J!�j]���޻��F#���Uw{ŐK�vSH3L�-1��=E��Pp8{?#���8/��"�L	N��\<ꩽr������j�a�� ��L���ơ;N�J�"�������V�j"zP	�jK�؄����Lɔ�s��7B������>o���Q�:n��Ys�;��X,Q2������Ȁ�+w��	,j`.��>@�쟕��w�t�:�������ى���F}�x���wB�D�O��������;�Z�+�-2��q��e�U��H\ /�󛯏���n#T�5�;߬B���w�nC��F���8	1�t�Ӝ5E��	�W�B�`��1���%l��xw{��o�nc(�
��a5����aF;G2�V'/}��E%�T�k/$G�R��;
M�p�v,K4"ƑG,ћ����Y#�w|]h��1�O�,&�QEůu9"��5q��0�
�㐍tQ�`n8j��AN�F����`c����]������ɲ��	��7G�C`����[���O�V�)��e�,i�?��=A^9�~�q�<y�� ��E����%�oeyP��g��z���p�`Q'���j*B�h | 5u�P"E^��������k���:���ߴ�;��p�:���*�2j<"%T�-Z��aDsƦDt��UJ%�2�B���A�w&	J���ʯ~7#���I�Э���>�#���H��) ��R	��>H�Y���@F=��9��3�ɛ�g��پѠM�Y�9H�ӡ0(&Ś�PhIÂqa�򗧾:C_�2H�$��I�FIB"�{;�p�����:!�惻���_w݀3��������x�r(�O5�K�0+��)�x�&"rڞl��H�f��s��]�d.<xF
�99����ˬ���(`��H���u�4b�$��%�E���v�:6��vh�_:љ<��`e`�9�}�PX,�Qw8?,��� ,�mb�*��/L�'�/n��ꝪF�%�]����՗������ �(���8< �N.Ca��C�&E(�/upR;�y��y��Ih���.V����8J�N+� t�"j�O.r0<�R�A�B���3�C"7Q��$|,f<Hl�<�b����Oi����s`��z��A�(:���S����([�&"�Ĉ
ŘT����:��s`;� �;�?v�w�:��Ҹ���,Zq늚$� S	�
�@�2 �&�D����'�����bT,��V$��#S���lm� �����d�����\D|�YaX�b���1өe}b�&��{��a���d�윚��4��?N�;��Sڮ�-�99	�u5]^s��98
w�����1D�ȥ��(����j_�]ڞۋm�=0#LV[Y�	��ۈ�H6ד��7���ф�=/,�b�5�?��~C/��<j�XrYlAP/Z���;�[�Cq�[�)���r�\L��H�RO�?x�~b.b��ܺ8��o:ި6�c���lg������U� O�F���39FX�z^�,�Hg۴0< �z�Jy�5<3oz�%~�b���g�I>��t�j#OZVǎ� l0��>f�DEq�rd��qE�Œΐ�ώ7�?xӨ���5��c�c=h��֘Y
�xN�P�'���H&�lU�Roh���&r,��L���B�<߿�t�Q���:� t�<��*��؉B��Hp��Di� E�`j|q0�hHR
���d�D���ݭ�77ʒY�h'����ud�q���p}Y� v  �}���F$F54	x����1h�#��B�GXn�撑���db�_7ʭ`c�J�Ș�.�-��e��^pM	цy�;�b���BՈ᭦�FbE��p����:�Fӵ��o�g�}K��B�(��Ǆ�ϫ�w�P�Fh�@�,� �6!��>��� �9��w+��F�k��\念��/�fu�g0p�	�dBw)I{���Մ^R� �Y� �� }u�p0��4�{����٥O�M(JT w��\�!8���r'��$�2d4�*kX0�-*��&���������F�5j��%�P��x1�^s�f`���GE!M�3(�IX�TQ�ذ�h��0�����8!�ػ�ٳF/sd����e�>%p��@�����@�	�bQr��z�$LaTۢ��x�Ӗ<�[����@u��=���`� ��$����������.j�W��֙y4��� b������5��Ѡ�����:��.e��|�RV�V�<��UV���4a����	�C��ѠZ�@���5�
I�@�x����7�F��#����<2[�j��@���/ }h��T�b��Hw���a�|�m��h���yn%wrܠ+˝X-Ĭ�B,S��Q���g��@���!���ԠK��ó �T�x�A��R����D�ݺd�z�h]�+?ի�h��	Y)�,<$�ց�@W2���Ub��	d;]<+�q@�bs�w���v�z�xu*ru���QF��+��	^��RO����:���]�]�n�~��(�W�b��v<�<xa��^�Y�/�\�&a�Y�`n��fMV�P��B�E�>%���k��.9���D�����~|���]�h�b]21ڢ�p+J�� ���n�L���*���p��j1ll��aYOerx0V���O3��iM�/����x2<�:���Uw� �0+������!婠�G����RP�}AV��0_���ݟl�4f���/X���]�p�ذ�q%�vZ�"�;���K ����ҩ&�h�A�������Tw�r��4Fu�UY������
�F*K"+#�e�XI���4A� �E�\��
���s��������C��=w����>n��� ;|�     