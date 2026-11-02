# Как развивался RoadMax

Описание публичного выпуска составлено с учётом 41 исторического отчёта и 5 документов передачи проекта, а также итоговой приёмки стрелок и файлов от 2 ноября 2026. Архивные поручения и остановки тестов рассматривались как история. Кандидатные и окончательные результаты разделены.

| Этап | Результат для пользователя |
| --- | --- |
| 1.1–1.2 | Стикеры, текст, карточки, фигуры, рисунки, магнитные связи, файлы и папки; перенос проектов с вложениями, дублирование и групповое оформление. Компактные панели, контекстные действия, подсказки и масштабирование. |
| 1.3 | Переработка истории действий, геометрии и обработки больших досок; атомарное хранение, резервные копии и проверки отказов; сохранение оригиналов вложений. |
| 1.4 | История транзакций и работа с ресурсами, улучшения мини-карты, сравнение производительности, длительные проверки и проверка установки/обновления. Финальные результаты 1.4 не переносятся автоматически на 1.5. |
| Редактор 1.5 | Изменение размеров изображений, смешанное дублирование, качество текста, мини-карта и автоматические связи. Ранний Smart Connectors был кандидатом; последующая приёмка движения выполнена отдельно. |
| Dashboard | Проекты, папки и доски, поиск по названиям, избранное, недавние, превью, корзина и возвращение к работе. |
| PDF | Встроенное чтение, поиск, заметки и пометки; удаление, вставка, перестановка, множественный выбор и поворот страниц; локальный экспорт. Затем — предпросмотр с доски, колесо, рука, временная рука по пробелу и вписывание двойным щелчком во всех инструментах. |
| Titanium | Новый знак и надпись RoadMax, светлая оболочка и оформление Dashboard. |
| Файлы, 2 ноября | Пересчёт автоматических стрелок по текущей сцене; редактор изображений; XLSX/CSV/TSV с формулами; локальный DOCX и PDF-экспорт. Неизменяемый оригинал и отдельная рабочая версия, перенос и отказоустойчивое сохранение. |

Подробности проверки нынешнего EXE — [VERIFICATION-1.5.0.md](VERIFICATION-1.5.0.md). Ни наличие функции в раннем отчёте, ни успешная компиляция сами по себе не означают завершённой приёмки всего продукта.

## Индекс рассмотренных исторических материалов

Имена и SHA-256 позволяют сопоставить описание с исходным сборником отчётов. Рабочие пути и содержимое закрытого репозитория здесь не публикуются.

- 01_Versions_1.1-1.2/01_QA-1.1.1.md — `dbfeecc5ee97822f4e7d8e6b612592c568e6f775f25e8b1a42b5550c048242a8`
- 01_Versions_1.1-1.2/02_QA-1.1.2.md — `a73637e9d7bd81151c84ca7c45f72d17d0eb08d519b7e9d873faba7e9836a2ec`
- 01_Versions_1.1-1.2/03_QA-1.1.3.md — `764ce0fe176b58e1d2d180521765e576c8854b31323239c4a54bd4c3f9c85d90`
- 01_Versions_1.1-1.2/04_QA-1.1.4.md — `b9283d86be3f0a2199e7aba2b6f8a66b5f60a18e6c03dcb67808c73bf07ea569`
- 01_Versions_1.1-1.2/05_Отчёт-RoadMax-1.2.0.md — `ff75604d6b4c92961af58b45d212e7584f1132635fea63e73e4cf874f70d1ff6`
- 01_Versions_1.1-1.2/06_Проверка-RoadMax-1.1.9.md — `f881c1bc1141559b5da23139f8336aea60530a866b9908419a02dba58d28c000`
- 01_Versions_1.1-1.2/07_ui-audit.md — `abd6818bd0d775d053157abeae4a1b8678e9b8917952dbf2cdfc8c2b1591370a`
- 02_Engine_1.3/01_ROADMAX_FINAL_ENGINEERING_REPORT.md — `c0f680e25ebfa2cb1d9b5cd89f7cf5503b6535e6259be16020918483099a2fca`
- 02_Engine_1.3/02_ENGINE_AUDIT.md — `8a67fda85d89479a75a2f60080efa551299473496d480eeb8a24b5f2f5814a30`
- 02_Engine_1.3/03_PERFORMANCE_BASELINE.md — `3ce29d207f8ede786ff3d239f667a9ae22e797c72251003c8ab11ccb62471161`
- 02_Engine_1.3/04_PERFORMANCE_RESULTS.md — `61c5d23628c897ee32d57a8c0bc4efbc6c792e0909a28e57edb7785b4167fecf`
- 02_Engine_1.3/05_TEST_REPORT.md — `49d500806c5410bd8444b89605b987f7925a67badc9ee110cb14b5cdd28fc3b2`
- 03_Candidate_1.4/01_LONG_SESSION_STABILITY.md — `ba124143b92ce2363495d36afa423f2c03f6c0486b1e1d8354dc634ed544e24e`
- 03_Candidate_1.4/02_MEMORY_PROFILING.md — `da2a681f274e7e3598cfeddea5c6955f303b6ca2f9a1cbd1c95899c57a554da7`
- 03_Candidate_1.4/03_PERFORMANCE_1_3_VS_1_4.md — `00505e0446125119c34bacbb6b262801e39c657f092a6c9dcb0485cf7efc7a91`
- 03_Candidate_1.4/04_RELEASE_READINESS_1_4.md — `b1a4fc9b595b15ab8781c1afc6731406f92ab2d247ab9252aa60f24051bff097`
- 03_Candidate_1.4/05_ROADMAX_1_4_ENGINEERING_REPORT.md — `934586364d6a4a852ed5409a614d6d7abdd7ad603544698f3482470969129ad4`
- 04_Release_1.4/01_REPORT.md — `0f7a6c78c49795828d65646e400c7dab3b0c35577514f3d3c415bbf6e963d7ee`
- 04_Release_1.4/02_LONG_SESSION_STABILITY.md — `20b29d94883253952b5ed3788b25b3b95fd38f44a815e724783e056b363578bd`
- 04_Release_1.4/03_MEMORY_PROFILING.md — `981617673817599eae3724b3a00b1ccf4012b63b7ef54db7646d0e280de6aa8d`
- 04_Release_1.4/04_PERFORMANCE_1_3_VS_1_4.md — `f3db3e8021bf123c10e38297d4c00e7701a4658e74b730a6789bdb79dbf3ebb7`
- 04_Release_1.4/05_RELEASE_READINESS_1_4.md — `24ce49f5ab6f377789b8de26df27ac291b692377b27a4870f3477c14fcfb531b`
- 04_Release_1.4/06_ROADMAX_1_4_ENGINEERING_REPORT.md — `225ab7947f55dcb8b55f50c40b90ebf627d5f719b2c2b71890735ae24c95cb76`
- 05_Editor_and_Connectors_1.5/01_SMART_CONNECTORS_ENGINEERING_REPORT.md — `44dec61d03f34f17eb8ac5732d1868ae1604ee85ce2093d9e88ead754e9e5aca`
- 05_Editor_and_Connectors_1.5/02_SMART_CONNECTORS_ROOT_CAUSE.md — `d98f010fc36a0e15d7ae4929179c240312e4c633559e4d74637345e0f29fb19c`
- 05_Editor_and_Connectors_1.5/03_ROADMAX_1_5_EDITOR_QUALITY_REPORT.md — `bfcc46371af6dc1a45389c6bb712e73b0dd68ce06b5b9a7c8663f0eca36f3af0`
- 06_Dashboard_and_Previews/01_ROADMAX_DASHBOARD_IMPLEMENTATION_REPORT.md — `1e27166aeb3dc52be30980a05708fd68094f6c0e5c4cd5968c93052bf0f52d61`
- 06_Dashboard_and_Previews/02_ROADMAX_INDEPENDENT_AUDIT.txt — `9834ef6a227ada57c7aea8e1f175bde919b367937b950d9feca076190dc470f6`
- 06_Dashboard_and_Previews/03_ROADMAX_STABILIZATION_AND_PREVIEWS_REPORT.md — `7c1c8e6c63ab9f3e74fc0d2d6011d273bebd89a2238f6db6f1d1c8576b76b76e`
- 07_PDF/01_ROADMAX_PDF_IMPLEMENTATION_REPORT.md — `af2c31963d4fd64f9f8631a6c04e314265c61d35018c512208846f31dd9697ca`
- 07_PDF/02_ROADMAX_PDF_PAGES_REPORT.md — `8d4f3d290ab0a3f6d56d03e4c17706d9769d00c40196d99b9a37d225534edf4e`
- 07_PDF/03_ROADMAX_PDF_MULTISELECT_REPORT.md — `ca12750dbef0d38daedbdd47a4cae465cfc23b20fd019ce152f9616022aaef9d`
- 07_PDF/04_ROADMAX_PDF_ROTATION_REPORT.md — `422084e87411bca1cb3b8781fb2805452efbf4f4d4ce2e4c1385b993fc962a5b`
- 07_PDF/05_ROADMAX_PDF_PREVIEW_ZOOM_REPORT.md — `ca57fc8daeb5eccc5b73b24ef3520899d8f88705421d4d374f63563bc8d3a9ce`
- 07_PDF/06_ROADMAX_PDF_EDITOR_ZOOM_REPORT.md — `f85cf1d65a4dadfa47dce8eb1ee2523b7935858d7dcd48f923b41c3e2b2b4fd0`
- 07_PDF/07_ROADMAX_PDF_SPACE_HAND_REPORT.md — `284aab9cecdb8c5ad7821c328867c345bcbe34f7e09e934a6167e583f489a429`
- 07_PDF/08_ROADMAX_PDF_DOUBLE_FIT_REPORT.md — `17858a9b77d7486408415f3fbfdec4cf9fd2ca4956d4fbc0d41714b247aa56cb`
- 07_PDF/09_ROADMAX_PDF_ALL_TOOLS_FIT_REPORT.md — `0f900317f25db471c04acc40cecce26e90b088a368e63988dfeb6eda0ef3aa02`
- 08_Project_Handoffs/01_PROJECT_HANDOFF.md — `52b0e9dbf319e86963298c81c7edf7ea0d4ef2a4f13ae5b76b01d52751508020`
- 08_Project_Handoffs/02_PROJECT_HANDOFF.md — `c2e0eab8f0195c6676813a5b81cfb27f9cdfa7561a1d3a2e81f8b347c5c97e7f`
- 08_Project_Handoffs/03_PROJECT_HANDOFF.md — `f3d8fecc89282b788bbdba42bc32907dd6b8227c686afadf274ab91ee21c0daa`
- 08_Project_Handoffs/04_PROJECT_HANDOFF.md — `f90ba3aeac787a3ace0d12a8f384daa6722413b3e0bda94494dd5c057f9148fc`
- 08_Project_Handoffs/05_PROJECT_HANDOFF.md — `b4e1eaaab6012a83bede2d6fb432f7d1fe2f577c1ca83c4b5396133327c120ac`
- 09_Other_Report_Revisions/01_PERFORMANCE_BASELINE.md — `9934ebb097ae1cdac0c7c8b89c86da260d7eac98460a3ddf5df9cac4590bd5eb`
- 09_Other_Report_Revisions/02_TEST_REPORT.md — `c84527b9df4648214092d1b7f552d9817f51a33adb4e942f0bc1f3632c4f8d31`
- 09_Other_Report_Revisions/03_ROADMAX_FINAL_ENGINEERING_REPORT.md — `944b5a830077f987069051fad95720355a5d5e1afc26e5c7c9569673d2db2978`
