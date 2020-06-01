import subprocess

def init_joplin(joplin_pass):
    subprocess.call(["joplin", "sync"])
    decrypted = True if subprocess.Popen(["joplin", "e2ee", "status"], stdout=subprocess.PIPE).communicate()[0] == "Encryption is: Disabled" else False
    if not decrypted:
        subprocess.call(["joplin", "e2ee", "decrypt", "-p", f"'{joplin_pass}'"])

def get_notes(note_tag):
    return subprocess.Popen(["joplin", "tag", "list", note_tag], stdout=subprocess.PIPE).communicate()[0].decode("utf-8")

def enumerate_iterable(iterable):
    iterable = [item.replace("[ ] ", "") for item in iterable if "[X]" not in item and item != ""]
    if len(iterable) == 1:
        return iterable[0]
    elif len(iterable) == 0:
        return []
    else:
        return ' és '.join([', '.join(iterable[:-1]), iterable[-1]])

def say(CONFIG):
    joplin_pass = CONFIG["joplin"]["password"]
    todo_tag = CONFIG["joplin"]["todoTag"]
    reminder_tag = CONFIG["joplin"]["reminderTag"]

    init_joplin(joplin_pass)

    todos =     enumerate_iterable(get_notes(todo_tag).split("\n"))
    reminders = enumerate_iterable(get_notes(reminder_tag).split("\n"))

    todos = ("Teendők listája: " + todos + ". ") if len(todos) >= 1 else "Nincs teendőd. "
    reminders = ("És ne felejtsd el hogy " + reminders + ". ") if len(reminders) >= 1 else ""
    return todos + reminders
