# coding=gbk
import math
import base64
import os
from tkinter import *
from tkinter import messagebox

YagiAntenna_PNG = "iVBORw0KGgoAAAANSUhEUgAAAZIAAAEGCAYAAABPdROvAAAAAXNSR0IArs4c6QAAFph0RVh0bXhmaWxlACUzQ214ZmlsZSUzRSUzQ2RpYWdyYW0lMjBpZCUzRCUyMm5KNnRWbFYxck4wUTNuSkQ0a2d6JTIyJTIwbmFtZSUzRCUyMiVFNyVBQyVBQyUyMDElMjAlRTklQTElQjUlMjIlM0UlM0NteEdyYXBoTW9kZWwlMjBkeCUzRCUyMjc0NiUyMiUyMGR5JTNEJTIyMzA4JTIyJTIwZ3JpZCUzRCUyMjElMjIlMjBncmlkU2l6ZSUzRCUyMjEwJTIyJTIwZ3VpZGVzJTNEJTIyMSUyMiUyMHRvb2x0aXBzJTNEJTIyMSUyMiUyMGNvbm5lY3QlM0QlMjIxJTIyJTIwYXJyb3dzJTNEJTIyMSUyMiUyMGZvbGQlM0QlMjIxJTIyJTIwcGFnZSUzRCUyMjElMjIlMjBwYWdlU2NhbGUlM0QlMjIxJTIyJTIwcGFnZVdpZHRoJTNEJTIyODI3JTIyJTIwcGFnZUhlaWdodCUzRCUyMjExNjklMjIlMjBiYWNrZ3JvdW5kJTNEJTIybm9uZSUyMiUyMG1hdGglM0QlMjIwJTIyJTIwc2hhZG93JTNEJTIyMCUyMiUzRSUzQ3Jvb3QlM0UlM0NteENlbGwlMjBpZCUzRCUyMjAlMjIlMkYlM0UlM0NteENlbGwlMjBpZCUzRCUyMjElMjIlMjBwYXJlbnQlM0QlMjIwJTIyJTJGJTNFJTNDbXhDZWxsJTIwaWQlM0QlMjIyJTIyJTIwdmFsdWUlM0QlMjIlMjIlMjBzdHlsZSUzRCUyMmVuZEFycm93JTNEbm9uZSUzQmh0bWwlM0QxJTNCJTIyJTIwcGFyZW50JTNEJTIyMSUyMiUyMGVkZ2UlM0QlMjIxJTIyJTNFJTNDbXhHZW9tZXRyeSUyMHdpZHRoJTNEJTIyNTAlMjIlMjBoZWlnaHQlM0QlMjI1MCUyMiUyMHJlbGF0aXZlJTNEJTIyMSUyMiUyMGFzJTNEJTIyZ2VvbWV0cnklMjIlM0UlM0NteFBvaW50JTIweCUzRCUyMjI3MCUyMiUyMHklM0QlMjI0MTAlMjIlMjBhcyUzRCUyMnNvdXJjZVBvaW50JTIyJTJGJTNFJTNDbXhQb2ludCUyMHglM0QlMjIyNzAlMjIlMjB5JTNEJTIyMTkwJTIyJTIwYXMlM0QlMjJ0YXJnZXRQb2ludCUyMiUyRiUzRSUzQyUyRm14R2VvbWV0cnklM0UlM0MlMkZteENlbGwlM0UlM0NteENlbGwlMjBpZCUzRCUyMjclMjIlMjB2YWx1ZSUzRCUyMiUyMiUyMHN0eWxlJTNEJTIyZW5kQXJyb3clM0Rub25lJTNCaHRtbCUzRDElM0IlMjIlMjBwYXJlbnQlM0QlMjIxJTIyJTIwZWRnZSUzRCUyMjElMjIlM0UlM0NteEdlb21ldHJ5JTIwd2lkdGglM0QlMjI1MCUyMiUyMGhlaWdodCUzRCUyMjUwJTIyJTIwcmVsYXRpdmUlM0QlMjIxJTIyJTIwYXMlM0QlMjJnZW9tZXRyeSUyMiUzRSUzQ214UG9pbnQlMjB4JTNEJTIyMzYwJTIyJTIweSUzRCUyMjM5MCUyMiUyMGFzJTNEJTIyc291cmNlUG9pbnQlMjIlMkYlM0UlM0NteFBvaW50JTIweCUzRCUyMjM2MCUyMiUyMHklM0QlMjIyMTAlMjIlMjBhcyUzRCUyMnRhcmdldFBvaW50JTIyJTJGJTNFJTNDJTJGbXhHZW9tZXRyeSUzRSUzQyUyRm14Q2VsbCUzRSUzQ214Q2VsbCUyMGlkJTNEJTIyOCUyMiUyMHZhbHVlJTNEJTIyJTIyJTIwc3R5bGUlM0QlMjJlbmRBcnJvdyUzRG5vbmUlM0JodG1sJTNEMSUzQiUyMiUyMHBhcmVudCUzRCUyMjElMjIlMjBlZGdlJTNEJTIyMSUyMiUzRSUzQ214R2VvbWV0cnklMjB3aWR0aCUzRCUyMjUwJTIyJTIwaGVpZ2h0JTNEJTIyNTAlMjIlMjByZWxhdGl2ZSUzRCUyMjElMjIlMjBhcyUzRCUyMmdlb21ldHJ5JTIyJTNFJTNDbXhQb2ludCUyMHglM0QlMjI0MDkuODMlMjIlMjB5JTNEJTIyMzkwJTIyJTIwYXMlM0QlMjJzb3VyY2VQb2ludCUyMiUyRiUzRSUzQ214UG9pbnQlMjB4JTNEJTIyNDA5LjgzJTIyJTIweSUzRCUyMjIxMCUyMiUyMGFzJTNEJTIydGFyZ2V0UG9pbnQlMjIlMkYlM0UlM0MlMkZteEdlb21ldHJ5JTNFJTNDJTJGbXhDZWxsJTNFJTNDbXhDZWxsJTIwaWQlM0QlMjIxMSUyMiUyMHZhbHVlJTNEJTIyJTIyJTIwc3R5bGUlM0QlMjJlbmRBcnJvdyUzRG5vbmUlM0JodG1sJTNEMSUzQiUyMiUyMHBhcmVudCUzRCUyMjElMjIlMjBlZGdlJTNEJTIyMSUyMiUzRSUzQ214R2VvbWV0cnklMjB3aWR0aCUzRCUyMjUwJTIyJTIwaGVpZ2h0JTNEJTIyNTAlMjIlMjByZWxhdGl2ZSUzRCUyMjElMjIlMjBhcyUzRCUyMmdlb21ldHJ5JTIyJTNFJTNDbXhQb2ludCUyMHglM0QlMjI1NTAlMjIlMjB5JTNEJTIyMzkwJTIyJTIwYXMlM0QlMjJzb3VyY2VQb2ludCUyMiUyRiUzRSUzQ214UG9pbnQlMjB4JTNEJTIyNTUwJTIyJTIweSUzRCUyMjIxMCUyMiUyMGFzJTNEJTIydGFyZ2V0UG9pbnQlMjIlMkYlM0UlM0MlMkZteEdlb21ldHJ5JTNFJTNDJTJGbXhDZWxsJTNFJTNDbXhDZWxsJTIwaWQlM0QlMjIxMiUyMiUyMHZhbHVlJTNEJTIyJTIyJTIwc3R5bGUlM0QlMjJlbmRBcnJvdyUzRG5vbmUlM0JkYXNoZWQlM0QxJTNCaHRtbCUzRDElM0JkYXNoUGF0dGVybiUzRDElMjAzJTNCc3Ryb2tlV2lkdGglM0QyJTNCJTIyJTIwcGFyZW50JTNEJTIyMSUyMiUyMGVkZ2UlM0QlMjIxJTIyJTNFJTNDbXhHZW9tZXRyeSUyMHdpZHRoJTNEJTIyNTAlMjIlMjBoZWlnaHQlM0QlMjI1MCUyMiUyMHJlbGF0aXZlJTNEJTIyMSUyMiUyMGFzJTNEJTIyZ2VvbWV0cnklMjIlM0UlM0NteFBvaW50JTIweCUzRCUyMjQ5MCUyMiUyMHklM0QlMjIyOTkuNjYwMDAwMDAwMDAwMSUyMiUyMGFzJTNEJTIyc291cmNlUG9pbnQlMjIlMkYlM0UlM0NteFBvaW50JTIweCUzRCUyMjUzMCUyMiUyMHklM0QlMjIzMDAuMDAwMDAwMDAwMDAwMDYlMjIlMjBhcyUzRCUyMnRhcmdldFBvaW50JTIyJTJGJTNFJTNDJTJGbXhHZW9tZXRyeSUzRSUzQyUyRm14Q2VsbCUzRSUzQ214Q2VsbCUyMGlkJTNEJTIyMTglMjIlMjB2YWx1ZSUzRCUyMiUyMiUyMHN0eWxlJTNEJTIyZW5kQXJyb3clM0Rub25lJTNCaHRtbCUzRDElM0IlMjIlMjBwYXJlbnQlM0QlMjIxJTIyJTIwZWRnZSUzRCUyMjElMjIlM0UlM0NteEdlb21ldHJ5JTIwd2lkdGglM0QlMjI1MCUyMiUyMGhlaWdodCUzRCUyMjUwJTIyJTIwcmVsYXRpdmUlM0QlMjIxJTIyJTIwYXMlM0QlMjJnZW9tZXRyeSUyMiUzRSUzQ214UG9pbnQlMjB4JTNEJTIyNDYwJTIyJTIweSUzRCUyMjM5MCUyMiUyMGFzJTNEJTIyc291cmNlUG9pbnQlMjIlMkYlM0UlM0NteFBvaW50JTIweCUzRCUyMjQ2MCUyMiUyMHklM0QlMjIyMTAlMjIlMjBhcyUzRCUyMnRhcmdldFBvaW50JTIyJTJGJTNFJTNDJTJGbXhHZW9tZXRyeSUzRSUzQyUyRm14Q2VsbCUzRSUzQ214Q2VsbCUyMGlkJTNEJTIyMjAlMjIlMjB2YWx1ZSUzRCUyMiVFNSU4RiU4RCVFNSVCMCU4NCVFNSU5OSVBOCUyMiUyMHN0eWxlJTNEJTIydGV4dCUzQmh0bWwlM0QxJTNCc3Ryb2tlQ29sb3IlM0Rub25lJTNCZmlsbENvbG9yJTNEbm9uZSUzQmFsaWduJTNEY2VudGVyJTNCdmVydGljYWxBbGlnbiUzRG1pZGRsZSUzQndoaXRlU3BhY2UlM0R3cmFwJTNCcm91bmRlZCUzRDAlM0IlMjIlMjBwYXJlbnQlM0QlMjIxJTIyJTIwdmVydGV4JTNEJTIyMSUyMiUzRSUzQ214R2VvbWV0cnklMjB4JTNEJTIyMjQwJTIyJTIweSUzRCUyMjQyMCUyMiUyMHdpZHRoJTNEJTIyNjAlMjIlMjBoZWlnaHQlM0QlMjIzMCUyMiUyMGFzJTNEJTIyZ2VvbWV0cnklMjIlMkYlM0UlM0MlMkZteENlbGwlM0UlM0NteENlbGwlMjBpZCUzRCUyMjIxJTIyJTIwdmFsdWUlM0QlMjIlRTYlOEMlQUYlRTUlQUQlOTAlMjIlMjBzdHlsZSUzRCUyMnRleHQlM0JodG1sJTNEMSUzQnN0cm9rZUNvbG9yJTNEbm9uZSUzQmZpbGxDb2xvciUzRG5vbmUlM0JhbGlnbiUzRGNlbnRlciUzQnZlcnRpY2FsQWxpZ24lM0RtaWRkbGUlM0J3aGl0ZVNwYWNlJTNEd3JhcCUzQnJvdW5kZWQlM0QwJTNCJTIyJTIwcGFyZW50JTNEJTIyMSUyMiUyMHZlcnRleCUzRCUyMjElMjIlM0UlM0NteEdlb21ldHJ5JTIweCUzRCUyMjMwMCUyMiUyMHklM0QlMjI0MjAlMjIlMjB3aWR0aCUzRCUyMjYwJTIyJTIwaGVpZ2h0JTNEJTIyMzAlMjIlMjBhcyUzRCUyMmdlb21ldHJ5JTIyJTJGJTNFJTNDJTJGbXhDZWxsJTNFJTNDbXhDZWxsJTIwaWQlM0QlMjIyMiUyMiUyMHZhbHVlJTNEJTIyJUU1JUJDJTk1JUU1JTkwJTkxJUU1JTk5JUE4JTIwMSUyQyUyMDIlMkMlMjAzJTIwLi4uLi4uJTIwbiUyMiUyMHN0eWxlJTNEJTIydGV4dCUzQmh0bWwlM0QxJTNCc3Ryb2tlQ29sb3IlM0Rub25lJTNCZmlsbENvbG9yJTNEbm9uZSUzQmFsaWduJTNEY2VudGVyJTNCdmVydGljYWxBbGlnbiUzRG1pZGRsZSUzQndoaXRlU3BhY2UlM0R3cmFwJTNCcm91bmRlZCUzRDAlM0IlMjIlMjBwYXJlbnQlM0QlMjIxJTIyJTIwdmVydGV4JTNEJTIyMSUyMiUzRSUzQ214R2VvbWV0cnklMjB4JTNEJTIyMzYwJTIyJTIweSUzRCUyMjQyMCUyMiUyMHdpZHRoJTNEJTIyMjAwJTIyJTIwaGVpZ2h0JTNEJTIyMzAlMjIlMjBhcyUzRCUyMmdlb21ldHJ5JTIyJTJGJTNFJTNDJTJGbXhDZWxsJTNFJTNDbXhDZWxsJTIwaWQlM0QlMjIzMyUyMiUyMHZhbHVlJTNEJTIyJTIyJTIwc3R5bGUlM0QlMjJlbmRBcnJvdyUzRG5vbmUlM0JodG1sJTNEMSUzQiUyMiUyMHBhcmVudCUzRCUyMjElMjIlMjBlZGdlJTNEJTIyMSUyMiUzRSUzQ214R2VvbWV0cnklMjB3aWR0aCUzRCUyMjUwJTIyJTIwaGVpZ2h0JTNEJTIyNTAlMjIlMjByZWxhdGl2ZSUzRCUyMjElMjIlMjBhcyUzRCUyMmdlb21ldHJ5JTIyJTNFJTNDbXhQb2ludCUyMHglM0QlMjI1NzAlMjIlMjB5JTNEJTIyMzEwJTIyJTIwYXMlM0QlMjJzb3VyY2VQb2ludCUyMiUyRiUzRSUzQ214UG9pbnQlMjB4JTNEJTIyNTcwJTIyJTIweSUzRCUyMjMxMCUyMiUyMGFzJTNEJTIydGFyZ2V0UG9pbnQlMjIlMkYlM0UlM0NBcnJheSUyMGFzJTNEJTIycG9pbnRzJTIyJTNFJTNDbXhQb2ludCUyMHglM0QlMjI2MDAlMjIlMjB5JTNEJTIyMzEwJTIyJTJGJTNFJTNDbXhQb2ludCUyMHglM0QlMjI2MDAlMjIlMjB5JTNEJTIyMjkwJTIyJTJGJTNFJTNDbXhQb2ludCUyMHglM0QlMjIyMDAlMjIlMjB5JTNEJTIyMjkwJTIyJTJGJTNFJTNDbXhQb2ludCUyMHglM0QlMjIyMDAlMjIlMjB5JTNEJTIyMzEwJTIyJTJGJTNFJTNDJTJGQXJyYXklM0UlM0MlMkZteEdlb21ldHJ5JTNFJTNDJTJGbXhDZWxsJTNFJTNDbXhDZWxsJTIwaWQlM0QlMjIzNCUyMiUyMHZhbHVlJTNEJTIyJTIyJTIwc3R5bGUlM0QlMjJlbmRBcnJvdyUzRG5vbmUlM0JodG1sJTNEMSUzQnN0YXJ0U2l6ZSUzRDYlM0IlMjIlMjBwYXJlbnQlM0QlMjIxJTIyJTIwZWRnZSUzRCUyMjElMjIlM0UlM0NteEdlb21ldHJ5JTIwd2lkdGglM0QlMjI1MCUyMiUyMGhlaWdodCUzRCUyMjUwJTIyJTIwcmVsYXRpdmUlM0QlMjIxJTIyJTIwYXMlM0QlMjJnZW9tZXRyeSUyMiUzRSUzQ214UG9pbnQlMjB4JTNEJTIyMzMwJTIyJTIweSUzRCUyMjQwMCUyMiUyMGFzJTNEJTIyc291cmNlUG9pbnQlMjIlMkYlM0UlM0NteFBvaW50JTIweCUzRCUyMjMzMCUyMiUyMHklM0QlMjIzMDUlMjIlMjBhcyUzRCUyMnRhcmdldFBvaW50JTIyJTJGJTNFJTNDJTJGbXhHZW9tZXRyeSUzRSUzQyUyRm14Q2VsbCUzRSUzQ214Q2VsbCUyMGlkJTNEJTIyMzUlMjIlMjB2YWx1ZSUzRCUyMiUyMiUyMHN0eWxlJTNEJTIyZW5kQXJyb3clM0Rub25lJTNCaHRtbCUzRDElM0IlMjIlMjBwYXJlbnQlM0QlMjIxJTIyJTIwZWRnZSUzRCUyMjElMjIlM0UlM0NteEdlb21ldHJ5JTIwd2lkdGglM0QlMjI1MCUyMiUyMGhlaWdodCUzRCUyMjUwJTIyJTIwcmVsYXRpdmUlM0QlMjIxJTIyJTIwYXMlM0QlMjJnZW9tZXRyeSUyMiUzRSUzQ214UG9pbnQlMjB4JTNEJTIyMzMwLjA1OTk5OTk5OTk5OTk1JTIyJTIweSUzRCUyMjI5NSUyMiUyMGFzJTNEJTIyc291cmNlUG9pbnQlMjIlMkYlM0UlM0NteFBvaW50JTIweCUzRCUyMjMzMCUyMiUyMHklM0QlMjIyMDAlMjIlMjBhcyUzRCUyMnRhcmdldFBvaW50JTIyJTJGJTNFJTNDJTJGbXhHZW9tZXRyeSUzRSUzQyUyRm14Q2VsbCUzRSUzQyUyRnJvb3QlM0UlM0MlMkZteEdyYXBoTW9kZWwlM0UlM0MlMkZkaWFncmFtJTNFJTNDJTJGbXhmaWxlJTNFCuauhgAAGxdJREFUeF7tnW+odVtVxp+bpF5vZXWverNuiUFFJVEUQhalIRlFRpfQqCiKKKICoSAUu76J1odI+gsRQVGhEgWmgRFpUQbVhz5EUUEiRGGmkKX36i0txuteb+vsd+0z55h7nzXWGuO34eXAO+dcc43feNZ81phr7XPuEZ9TBB6RdAs8EIAABCBwPYF7AHSSwP9Kgg8CgQAEINAgwEJ5GhBGwuUDAQhAoIMARoKRdMiELhCAAAROE8BIMBKuDwhAAAJnEcBIMJKzBMRgCEAAAhgJRsJVAAEIQOAsAhgJRnKWgBgMAQhAACPBSLgKIAABCJxFACPBSM4SEIMhAAEIYCQYyUSAb/KzHkAAAkMEMBKMZCLAFzCHLiEGQQACGAlGgpGwDkAAAmcRwEgwkonARyU9QZJVJnwgAAEIdBPASDASjKT7cqEjBCCwRAAjwUgwEtYGCEDgLAIYCUaCkZx1CTEYAhDASDASjIR1AAIQOIsARoKRYCRnXUIMhgAEMBKMZCLwEUkfL8ne3uIDAQhAoJsARoKRRBtJhm/Uf6GkhyXd6r7yttsxQz62S/f/zywVZ4wEI4k2kgzfqDcjeb2k5+xhBWucY4Z87CENqThjJBgJRnL+soORnM+w2hEwkiIZT5XojpxFPSPJwBkj6RAYXa4QyKD7OwFRkVCRUJGcv8JhJOczrHYEjKRIxlMluiNnVpE8UZL9XPOTgTNGsqZicsyVQfdUJB1aTJXojnj/R9KTMJIOUnd3wUiGsJUelGp9YWuLra2JAEYyvq5hJOPsqo7ESIpkPlWiO3KGkXRAOtEFIxlnV3VkqvWFioSKhIrk/KUMIzmfYbUjYCRFMp4q0R05oyLpgERFMg6JkVcIpFpfqEioSOYVyZMlmaGs+clwQVGRrKmYHHNl0P2dTGAkGMlE4L8l3YuRDK1SGMkQttKDMJIi6U+V6I6cYSQdkNjaGofESLa2KmoAI1kn6xk4U5Gso5VMs2TQPVtbHYpMleiOeKlIOiBRkYxDYiQVSUUNYCTrZD0DZyqSdbSSaZYMuqci6VBkqkR3xGsVyVMk2c81Pxk4YyRrKibHXBl0j5F0aDFVojvifVzSfRhJB6m7u2AkQ9hKD0q1vvD672ktp0p0xyWLkXRA4hnJOCRG8oykogYwknWynoEzFck6Wsk0Swbds7XVochUie6Il4qkAxIVyTgkRlKRVNQARrJO1jNwpiJZRyuZZsmgeyqSDkWmSnRHvFaRfIIk+7nmJwNnjGRNxeSYK4PuMZIOLaZKdEe8H5b0iRhJB6m7u2AkQ9hKD0q1vvDW1mktp0p0xyWLkXRA4hnJOCRG8oykogYwknWynoEzFck6Wsk0Swbds7XVochUie6Il4qkAxIVyTgkRlKRVNQARrJO1jNwpiJZRyuZZsmgeyqSDkWmSnRHvFaRfJIk+7nmJwNnjGRNxeSYK4PuMZIOLaZKdEe8GEkHJLa2xiExkq2tihqoZiQfkvRUKpIhqVORDGErPSjV+sLrv6e1nCrRHZcsRtIBiYpkHBIjqUgqagAjWSfrGThTkayjlUyzZNA9z0g6FJkq0R3xUpF0QKIiGYfESCqSihqoaCSfLMkMZc1PBs5UJGsqJsdcGXRPRdKhxVSJ7ojXDAQj6QC10AUjGeNWeVSq9YWH7aelnCrRHVfsY5I+hYqkg9TdXTCSIWylB6VaXzASjGQigJGMr2sYyTi7qiMxkiKZT5XojpxhJB2QeNg+DomRPGyvqAGMZJ2sZ+BMRbKOVjLNkkH3PGzvUGSqRHfEaxXJp0qyn2t+MnDGSNZUTI65MugeI+nQYqpEd8SLkXRAYmtrHBIj2dqqqIFqRvKopPupSIakTkUyhK30oFTrC29tndZyqkR3XLIYSQckKpJxSIykIqmoAYxknaxn4ExFso5WMs2SQfc8I+lQZKpEd8RLRdIBiYpkHBIjqUgqaqCikTwgyQxlzU8GzlQkayomx1wZdE9F0qHFVInuiNcMBCPpALXQBSMZ41Z5VKr1hYftp6WcKtEdVyxG0gGJra1xSIxka6uiBqoZyQclPY2trSGpU5EMYSs9KNX6QkVCRTIRwEjG1zWMZJxd1ZEYSZHMp0p0R84wkg5IbG2NQ2IkW1sVNVDRSJ4uyQxlzU8GzlQkayomx1wZdH8nE2xtsbU139rCSMYWKYxkjFvlURhJkeynSnRHzqwSwUg6QC10wUjGuFUelWp9oSKhIpkIfEDSM9jaGlrbMJIhbKUHYSRF0p8q0R05w0g6IPGwfRwSI3nYXlEDGMk6Wc/AmYpkHa1kmiWD7nnY3qHIVInuiNcqkgcl2c81Pxk4YyRrKibHXBl0j5F0aDFVojvixUg6ILG1NQ6JkWxtVdQARrJO1jNwpiJZRyuZZsmgeyqSDkWmSnRHvP8l6dPY2uogdXcXjGQIW+lBqdYXXv89reVUie64ZDGSDkhsbY1DYiRbWxU1gJGsk/UMnKlI1tFKplky6J6trQ5Fpkp0R7xWkTxTkv1c85OBM0aypmJyzJVB9xhJhxZTJbojXoykAxJbW+OQGMnWVkUNYCTrZD0DZyqSdbSSaZYMuqci6VBkqkR3xPufkj6dra0OUnd3wUiGsJUelGp94a2t01pOleiOSxYj6YDE1tY4JEaytVVRAxjJOlnPwJmKZB2tZJolg+7Z2upQZKpEd8RrFclnSLKfa34ycMZI1lRMjrky6B4j6dBiqkR3xIuRdEBia2scEiPZ2qqoAYxknaxn4ExFso5WMs2SQfdUJB2KTJXojnipSDogUZGMQ2IkFUlFDVQzkvdLeohnJENSpyIZwlZ6UKr1hdd/T2s5VaI7LlmMpAMSFck4JEZSkVTUQEUj+UxJZihrfjJwpiJZUzE55sqge56RdGgxVaI74jUDwUg6QC10wUjGuFUelWp9YWuLra2JAEYyvqxhJOPsqo4sYSRfJukbJX25pM+R9DRJPynpVVWzTtwQgAAEihH4iKQPSnqvpH+W9HeS/kLSWyX925zFcUXyBZJeK+k5kt4g6e2S/lbSuyV9tBjEVHcMHbn7D0mfxTOSDlJ3d6EiGcJWetBe1pePk/R0SZ8t6YslvUDSN0j6eUkvl/Rhy+LcSL5e0m9LeoWk15VO8ceC30uiL5UqjGScJEYyzq7qyD2vL/cfCo7Pl/Q1kh6fjMQqkb+S9C2Sfr9qZo/i3nOiR1KIkYxQ+9gYjGScXdWRGdaXX5FkZvK8yUjeJOmPqUSuaDpDoj0XqRnJsyTZzzU/GThjJGsqJsdcGXT/oKTX2/N0MxJ7sP5GSc/OkZ+LRZEh0R4Yj0j6WYzEg+xOX4xkCFvpQVnWF3uO/nwzkldLesLhwUnpzBbf2orKfYYLCiOJUs9+582ge6N/Ow4zkj+S9FOS/nC/ObmRM8+S6BuBc8GDZuCMkVxQEEUOlUH3V4zE3g9+rqR/LZLA3jCzJLo33qh+GThjJFHq2e+8GXR/xUg+JOkpBb8n0pJglkS34oxuz8AZIzlfRd8lyZ7T/ZqkWwuHs/bvlPTrhz7HXVrtX30Y/ycnxlv7V0mydnvx6KY/GXR/xUiyBHTpxMPl0kSXj5eBM0ZyvlbMROw3Z9i/JSOJbj8/wqtHyKB7i8jycsuekWQJiERfmsA6x8ugP4zkfK3Yq+f2edeJQ1m7/bP2pT6tdqs4rI9VG0vjqUj8ObRvvT8q6ckYyWl4GRY4vzTWH5GBM0ayvm72PmMG3T/z8Lu3HsJIMJLoCzLDBYWRRKtof/Nn0P0LJf2Y/ZoUjAQjib4EM1xQGEm0ivY3fwbd2y/4td8Q/EozktvfTNxfHm78jDMk2gPp9kMzz4AL9c3AGSO5kBgKHSaD7t8p6SX2exonI/nWw6+KL5THZqgZEt0MctYhKt6oeT1sWn0xkhYh2o8J7F33L5NkLyi82AIzI3nH4Q+WfC+5vkJg74n2pjMq3qh5vXyu64+RXJJmjWPtWffTnxyx39Nof6/qtpE88fBrUuyvX9kfKnlfjTw2o9xzopvBLXSIijdq3hFGp8ZgJJekWeNYe9W9VSKvOf6TI9OvkX/S4Q+V/JCkt0h6m6S/lvRPkt5T9Fvve0306GUYFW/UvKOclsZhJJekWeNYe9C9fU/EflW8/b0qe47+Ukl/cyg4blci0+f4T+0+Q9KLDr97y/5gyUOSHpB03+G3BPM322uInCghAIF9EbAvWtozi0t+7M/o/rukf5T055J+7/AHEO+a49hITp3EvZIeu+QZ7uBYe7hjuCTGqHij5r0kOyqSS9Kscayt694eeTzem4peI+k9XqZ+W0/0pVlHxRs17yX5YSSXpFnjWBl0f3Jrq0YK+6JMleiOkKPijZq3A0l3F4ykGxUdDwQy6B4j6ZBzqkRvON4MnDGSDoHR5QqBDLrHSDpEnSrRG443A2eMpENgdMFIKmogwwLnyVtUvFHzeti0+mIkLUK0HxPIoHsqkg5dp0r0huPNwBkj6RAYXahIKmogwwLnyVtUvFHzeti0+mIkLUK0U5EU1UCGBc6Tuqh4o+b1sGn1xUhahGjHSIpqIMMC50ldVLxR83rYtPpiJC1CtGMkRTWQYYHzpC4q3qh5PWxafTGSFiHaMZKiGsiwwHlSFxVv1LweNq2+GEmLEO0YSVENZFjgPKmLijdqXg+bVl+MpEWIdoykqAYyLHCe1EXFGzWvh02rL0bSIkQ7RlJUAxkWOE/qouKNmtfDptUXI2kRoh0jKaqBDAucJ3VR8UbN62HT6ouRtAjRjpEU1UCGBc6Tuqh4o+b1sGn1xUhahGjHSIpqIMMC50ldVLxR83rYtPpiJC1CtGMkRTWQYYHzpC4q3qh5PWxafTGSFiHaMZKiGsiwwHlSFxVv1LweNq2+GEmLEO0YSVENZFjgPKmLijdqXg+bVl+MpEWIdoykqAYyLHCe1EXFGzWvh02rL0bSIkQ7RlJUAxkWOE/qouKNmtfDptUXI2kRoh0jKaqBDAucJ3VR8UbN62HT6ouRtAjRjpEU1UCGBc6Tuqh4o+b1sGn1xUhahGjHSIpqIMMC50ldVLxR83rYtPpiJC1CtGMkRTWQYYHzpC4q3qh5PWxafTGSFiHaMZKiGsiwwHlSFxVv1LweNq2+GEmLEO0YSVENZFjgPKmLijdqXg+bVl+MpEWIdoykqAYyLHCe1EXFGzWvh02rL0bSIkQ7RlJUAxkWOE/qouKNmtfDptUXI2kRoh0jKaqBDAucJ3VR8UbN62HT6ouRtAjRjpEU1UCGBc6Tuqh4o+b1sGn1xUhahGjHSIpqIMMC50ldVLxR83rYtPpiJC1CtGMkRTWQYYHzpC4q3qh5PWxafTGSFiHaMZKiGsiwwHlSFxVv1LweNq2+GEmLEO0YSVENZFjgPKmLijdqXg+bVl+MpEWIdoykqAYyLHCe1EXFGzWvh02rL0bSIkQ7RlJUAxkWOE/qouKNmtfDptUXI2kRoh0jKaqBDAucJ3VR8UbN62HT6ouRtAjRjpEU1UCGBc6Tuqh4o+b1sGn1xUhahGjHSIpqIMMC50ldVLxR83rYtPpiJC1CtGMkRTWQYYHzpC4q3qh5PWxafTGSFiHaMZKiGsiwwHlSFxVv1LweNq2+GEmLEO0YSVENZFjgPKmLijdqXg+bVl+MpEWIdoykqAYyLHCe1EXFGzWvh02rL0bSIkQ7RlJUAxkWOE/qouKNmtfDptUXI2kRoh0jKaqBDAucJ3VR8UbN62HT6ouRtAjRjpEU1UCGBc6Tuqh4o+b1sGn1xUhahGjHSIpqIMMC50ldVLxR83rYtPpiJC1CtGMkRTWQYYHzpC4q3qh5PWxafTGSFiHaMZKiGsiwwHlSFxVv1LweNq2+GEmLEO0YSVENZFjgPKmLijdqXg+bVl+MpEWIdoykqAYyLHCe1EXFGzWvh02rL0bSIkQ7RlJUAxkWOE/qouKNmtfDptUXI2kRoh0jKaqBDAucJ3VR8UbN62HT6ouRtAjRjpEU1UCGBc6Tuqh4o+b1sGn1xUhahGjHSIpqIMMC50ldVLxR83rYtPpiJC1CtGMkRTWQYYHzpC4q3qh5PWxafTGSFiHaMZKiGsiwwHlSFxVv1LweNq2+GEmLEO0YSVENZFjgPKmLijdqXg+bVl+MpEWIdoykqAYyLHCe1EXFGzWvh02rL0bSIkQ7RlJUAxkWOE/qouKNmtfDptUXI2kRoh0jKaqBDAucJ3VR8UbN62HT6ouRtAjRjpEU1UCGBc6Tuqh4o+b1sGn1xUhahGjHSIpqIMMC50ldVLxR83rYtPpiJC1CtGMkRTWQYYHzpC4q3qh5PWxafTGSFiHaMZKiGsiwwHlSFxVv1LweNq2+GEmLEO0YSVENZFjgPKmLijdqXg+bVl+MpEWIdoykqAYyLHCe1EXFGzWvh02rL0bSIkQ7RlJUAxkWOE/qouKNmtfDptUXI2kRoh0jKaqBDAucJ3VR8UbN62HT6ouRtAjRjpEU1UCGBc6Tuqh4o+b1sGn1xUhahGjHSIpqIMMC50ldVLxR83rYtPpiJC1CtGMkRTWQYYHzpC4q3qh5PWxafTGSFiHaMZKiGsiwwHlSFxVv1LweNq2+GEmLEO0YSVENZFjgPKmLijdqXg+bVl+MpEWIdoykqAYyLHCe1EXFGzWvh02rL0bSIkQ7RlJUAxkWOE/qouKNmtfDptUXI2kRoh0jKaqBDAucJ3VR8T4i6ZbnRDfY14zk4QRxGNoM+digRO46pVSc79kD8aBzjFpYg8JVtXijODMvBNIRwEhOp7Tawlot3nQXMwFBIIoARoKRTAQwkqirkHkhsHMCGAlGgpHs/CLm9CEQTQAjwUgwkuirkPkhsHMCGAlGgpHs/CLm9CEQTQAjwUgwkuirkPkhsHMCGAlGgpHs/CLm9CEQTQAjwUgwkuirkPkhsHMCGAlGMhFI9U3bnV+XnD4EdkUAI8FIdiVYThYCENgeAYwEI9meKjkjCEBgVwQwEoxkV4LlZCEAge0RwEgwku2pkjOCAAR2RQAjwUh2JVhOFgIQ2B4BjAQj2Z4qOSMIQGBXBDASjGRXguVkIQCB7RHASDCS7amSM4IABHZFACPBSHYlWE4WAhDYHgGM5HRO+Kb39vTKGUEAAhskgJFsMCmcEgQgAIE9EcBI9pQtzhUCEIDABglgJBtMCqcEAQhAYE8EMJI9ZYtzhQAEILBBAhjJBpPCKUEAAhDYEwGMZE/Z4lwhAAEIbJAARrLBpHBKEIAABPZEACPZU7Y4VwhAAAIbJICRbDApnBIEIACBPRHASPaULc4VAhCAwAYJYCQbTAqnBAEIQGBPBDCSPWWLc4UABCCwQQIYyQaTwilBAAIQ2BMBjGRP2eJcIQABCGyQAEaywaRwShCAAAT2RAAj2VO2OFcIQAACGySAkWwwKZwSBCAAgT0RwEj2lC3OFQIQgMAGCVQzkvsl/Zakr5X0B5K+TdL7Dnl5paS3SXrHQp6sn31s7L2SXifp+2b9vkLSsyT95uz/flnSyyQ9Fpj35x3O63cXznl+Wt9+iM3inMewdOo/LunVgTFtaWrj+2cLJzTxtKYpB6ad44+1veAannvS2pbywrmsTCCrkZy6wI/Nw3DPzWXCb8YwN5RjI/kRSb90MCFre9dhwZ7Mxo75A5J+ekNGckvSr0r6hwGNTQuaDY02x4HTX3XIsXFcZySTdpZuXuykjfsltPa5kl4l6QdnN06noBybV+8N0fwmhJuNVSUXP1lmI7EKYeku8Jj68aJvF8R9ByP4oqPOdlG9XNJrd1CRWIX1E4fzf4Ok9x+qEq+RGI8flfSSQROKV/m6Z3CdkSzdtCyd3XTD8+gFql8zkTdKevdRBX6KylL1/aeNa8nm+B5JjxwOahV7a8y6WWG2GyWAkfgrkqWETBffWyX9wuHuz7tg30Si51tbVpHYna/9nBvkUpU2nct1d9M3cb57O+bS1pPFcGpry4zkNZJecU1l0Orj0Zrl7xcPC/xLOyuS4xzYfF/prERtzLNX3gKdcvEvsxsoKqOVrqjMRrK0dz3HOl3sSxXJeyS9cLYVNL9L63mOMM3Tuy1wU+k+NhLv1hZGcn1mlhb9VkUyGcmLFp5HmSbtZuS6PqfO6Dqteba2jo9vla19ep+LTQv62hXJ8fbrlxxMlEr6plaX2XEzG4ltbdnHnl/M96Anwf3G4f9PPSN576xc/+bDsY63yqaxdiy7A/NccCuk9/bLBPbw3La27GN3pUuf75b03KPtuuvOL9og12DXM8d8S+fUSxVzY5kbjxmJfSZNzSuNparlHK2NGomduxnJ/KWU67hMzyavq3J7uI70OTYw47Wl3YGRmHYzJruRzO/uprezjsvupYpkMp+lB+nzZw/HF8zxQ/6oBXe+5WJ3ufbWlj20tb1yu0N7s6TnH/bfXyzp7088/6Aiuf5SPvVSx3xL5RwjsRc2pudc52htxEimbbGRO3qvAV1iwVy6QcRILkG24xhZjWT+NoxdRD8n6YclPXB0h3Vqj7v11tbS67+Ge76dFmUi87RPi9hkqD9zMBJ748zueu0VZvv3Oyf27DGSjovoqMslt7ZOPWz3as1rJHb9fIejEjmmNL/m1npWiJH4tXqxERmNxAR1/Kprz5sr06uWH5D0lwOv/1pSpjfFtvb6r1VY9n0FM5DptWTbQ7bF4rrXeTES/6U2f55mo3srkmmm+faXGcnS679erXmMZKSasDFzLY08oPeTvjoCIzmX4BnjMxrJkqjtOYFtN9jn4YVXWedl/JcuPFfp+UKi9y7xjLR1D50WMXt+Y1+2tOc+ZhxPlfSWw1Guu/PESLpR3+l4/MXWU0YybbUez3BsJJeofo+N5LrnB/Ot2+ncpuraTO2dJ14Fnr+EcuoZyfG8Ntd0vPk52rzzbalT/eYMMRK/Vi82IqOR2EL5dknff9i2mb+KaeDm21mTudj/2926Pfh88GA0tugufQv+1JfEvHeJF0viwoHmMX6TpK87vHL6eQtvshx/u/p4u+94m+8mz3uPx56q3emV6uMtzV4jmR9nOobxuERFssT1umdjp/Jg52gaetMeE8U53xyBjEZyc7Q4MgRyELCbBatE7W1Dz6/wGTGfHMSI4loCGAkCgQAEIACBswhgJGfhYzAEIAABCGAkaAACEIAABM4igJGchY/BEIAABCCAkaABCEAAAhA4iwBGchY+BkMAAhCAAEaCBiAAAQhA4CwCGMlZ+BgMAQhAAAIYCRqAAAQgAIGzCGAkZ+FjMAQgAAEIYCRoAAIQgAAEziLwfyiM3G4jgxkyAAAAAElFTkSuQmCC"

ElmDiam_List = [0.001, 0.003, 0.005, 0.007, 0.01, 0.015, 0.02]
DirLen_Fact = [[0.4711, 0.018, 0.08398, 0.965], [0.462, 0.01941, 0.08543, 0.969], [0.4538, 0.02117, 0.0951, 1.00], [0.4491, 0.02274, 0.08801, 0.90], \
               [0.4421, 0.02396, 0.1027, 1.038], [0.4358, 0.02558, 0.1149, 1.03], [0.4268, 0.02614, 0.1112, 1.036]]
DirSpan_Fact = [0.075, 0.180, 0.215, 0.250, 0.280, 0.300, 0.315, 0.330, 0.345, 0.360, 0.375, 0.390, 0.400, 0.400]

temp = open('temp.png','wb+')
tempb64 = base64.b64decode(YagiAntenna_PNG)
temp.write(tempb64)
temp.close()

root = Tk()
root.title("八木天线计算器 by BG8LRD")

ant_img = PhotoImage(file="temp.png")
Label(root, image=ant_img).grid(columnspan=6)

os.remove("temp.png")

Label(root, text="中心频率(MHz)").grid(row=1, column=0)
freq_entry = Entry(root)
freq_entry.grid(row=1, column=1)

Label(root, text="元件直径(mm)").grid(row=1, column=2)
elm_diam_entry = Entry(root)
elm_diam_entry.grid(row=1, column=3)

Label(root, text="单元数量").grid(row=1, column=4)
elm_num_entry = Entry(root)
elm_num_entry.grid(row=1, column=5)

def read_entry():
    try:
        wave_len = 299793 / float(freq_entry.get())

        elm_diam = float(elm_diam_entry.get())
        if elm_diam < 0.001 * wave_len:
            messagebox.showwarning("警告", "直径不得小于" + str('%.1f'%(0.001 * wave_len)) + "mm")
        elif elm_diam > 0.02 * wave_len:
            messagebox.showwarning("警告", "直径不得大于" + str('%.1f'%(0.02 * wave_len)) + "mm")
        elm_diam /= 1000

        elm_num = int(elm_num_entry.get())
        if elm_num < 2:
            messagebox.showwarning("警告", "单元数量必须大于2")
        elif elm_num > 14:
            messagebox.showwarning("警告", "单元数量必须小于14")
        elm_num -= 2

        ref_len = ((-20 / (186.8769 * math.log(2 / elm_diam) - 320)) + 1) / 2 * wave_len
        
        dip_len = (0.4777 - (1.0522 * elm_diam) + (0.43363 * math.pow(elm_diam, -0.014891))) / 2 * wave_len
        dip_span = wave_len * 0.2

        dir_len = [0] * elm_num
        dir_span = [0] * elm_num

        for i in range(7):
            if elm_diam == float(ElmDiam_List[i]):
                for j in range(elm_num):
                    dir_len[j] = (float(DirLen_Fact[i][0]) - float(DirLen_Fact[i][1]) * math.log(j+1)) * \
                        (1 - float(DirLen_Fact[i][2]) * math.exp(-float(DirLen_Fact[i][3]) * (j+1))) * wave_len
            elif elm_diam > float(ElmDiam_List[i]) and elm_diam < float(ElmDiam_List[i+1]):
                for j in range(elm_num):
                    low_len = (float(DirLen_Fact[i][0]) - float(DirLen_Fact[i][1]) * math.log(j+1)) * \
                        (1 - float(DirLen_Fact[i][2]) * math.exp(-float(DirLen_Fact[i][3]) * (j+1)))
                    high_len = (float(DirLen_Fact[i+1][0]) - float(DirLen_Fact[i+1][1]) * math.log(j+1)) * \
                        (1 - float(DirLen_Fact[i+1][2]) * math.exp(-float(DirLen_Fact[i+1][3]) * (j+1)))
                    intp_fact = (elm_diam - float(ElmDiam_List[i])) / (float(ElmDiam_List[i+1]) - float(ElmDiam_List[i]))
                    dir_len[j] = low_len - intp_fact * (high_len - low_len) * wave_len
        
        for i in range(elm_num):
            dir_span[i] = float(DirSpan_Fact[i]) * wave_len
        
        boom_len = dip_span
        for i in range(elm_num):
            boom_len += float(dir_span[i])
        if boom_len < 0.2 * wave_len:
            messagebox.showwarning("警告", "天线总长过短,请增加单元")
        elif boom_len > 39 * wave_len:
            messagebox.showwarning("警告", "天线总长过长,请减少单元")
        
        Label(root, text="反射器长度(mm)").grid(row=2, column=0)
        ref_len_label = Label(root)
        ref_len_label.config(text='%.1f'%ref_len, fg='red')
        ref_len_label.grid(row=2, column=1)

        Label(root, text="振子长度(mm)").grid(row=2, column=2)
        dip_len_label = Label(root)
        dip_len_label.config(text='%.1f'%dip_len, fg='red')
        dip_len_label.grid(row=2, column=3)

        Label(root, text="振子与反射器间距(mm)").grid(row=2, column=4)
        dip_span_label = Label(root)
        dip_span_label.config(text='%.1f'%dip_span, fg='red')
        dip_span_label.grid(row=2, column=5)
        
        Label(root, text="引向器1长度(mm)").grid(row=3, column=0)
        dip_span_label = Label(root)
        dip_span_label.config(text='%.1f'%dir_len[0], fg='red')
        dip_span_label.grid(row=3, column=1)

        Label(root, text="引向器1与振子间距(mm)").grid(row=3, column=2)
        dip_span_label = Label(root)
        dip_span_label.config(text='%.1f'%dir_span[0], fg='red')
        dip_span_label.grid(row=3, column=3)
        
        Label(root, text="振子两导体间距小于(mm)").grid(row=3, column=4)
        dip_span_label = Label(root)
        dip_span_label.config(text='%.1f'%(wave_len / 80), fg='red')
        dip_span_label.grid(row=3, column=5)

        for i in range(1, elm_num):
            Label(root, text="引向器" + str(i+1) + "长度(mm)").grid(row=3+i, column=0)
            dip_span_label = Label(root)
            dip_span_label.config(text='%.1f'%dir_len[i], fg='red')
            dip_span_label.grid(row=3+i, column=1)
            Label(root, text="引向器" + str(i+1) + "与引向器" + str(i) + "间距(mm)").grid(row=3+i, column=2)
            dip_span_label = Label(root)
            dip_span_label.config(text='%.1f'%dir_span[i], fg='red')
            dip_span_label.grid(row=3+i, column=3)
        
    except:
        messagebox.showwarning("警告", "请输入正确格式")

Button(root, text="计 算", command=read_entry).grid(row=0, column=5)

root.mainloop()
