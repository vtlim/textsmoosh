import sys
from flask import Flask, request, render_template

app = Flask(__name__)

@app.route('/')
def my_form():
    return render_template('mainpage.html')

@app.route('/', methods=['POST'])
def my_form_post():
    text = request.form['text']

    # split text by line breaks
    input_lines = text.splitlines()

    if 'ignore-blank-lines' in request.form:
        nonblank_lines = []
        for line in input_lines:
            if line.strip() != "":
                nonblank_lines.append(line)
        input_lines = nonblank_lines

    if ('keep-trailing-spaces' not in request.form) and (
       'keep-leading-spaces' not in request.form):
        no_space_ends = []
        for line in input_lines:
            no_space_ends.append(line.strip())
        input_lines = no_space_ends

    elif 'keep-leading-spaces' not in request.form:
        no_space_lead = []
        for line in input_lines:
            no_space_lead.append(line.lstrip())
        input_lines = no_space_lead

    elif 'keep-trailing-spaces' not in request.form:
        no_space_trail = []
        for line in input_lines:
            no_space_trail.append(line.rstrip())
        input_lines = no_space_trail

    num_rm_start = int(request.form['rm-start'])
    if num_rm_start > 0:
        trimmed_lines = []
        for line in input_lines:
            trimmed_lines.append(line[num_rm_start:])
        input_lines = trimmed_lines

    num_rm_end = int(request.form['rm-end'])
    if num_rm_end > 0:
        trimmed_lines = []
        for line in input_lines:
            trimmed_lines.append(line[:-num_rm_end])
        input_lines = trimmed_lines

    if 'remove-all-spaces' in request.form:
        no_space_any = []
        for line in input_lines:
            no_space_any.append( ''.join(line.split()) )
            #no_space_any.append(re.sub(r"\s+", "", line))
        input_lines = no_space_any

    delim = request.form['delimiter']

    # use <pre> tag to preserve whitespace (multiple space, tabs, etc.)
    return "<pre>" + delim.join(input_lines) + "</pre>"

