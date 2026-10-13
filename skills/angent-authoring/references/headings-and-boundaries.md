# Headings and section boundaries

Headings exist to expose the structure of the subject.

## Good heading functions

A heading can name:
- a component/subsystem;
- a mechanism;
- a state or transition;
- an interface/boundary;
- a failure mode;
- a comparison;
- a procedure;
- a concrete case study;
- an integration problem.

Examples of useful shapes:

- `Device Tree binding của MCP2515`
- `Đường dữ liệu từ socket CAN đến SPI driver`
- `Khi module đã build nhưng không có trong rootfs`
- `Rollback schema khi hai phiên bản ứng dụng cùng tồn tại`

## Weak heading functions

Avoid headings whose main content is:
- author intention;
- advice to the writer/reader;
- drama or slogan;
- a conclusion before the section establishes it;
- process metadata about how the text was produced.

Examples of weak shapes:

- “Đừng đoán từ trí nhớ”
- “Bắt đầu từ điều quan trọng nhất”
- “Bây giờ hãy nhìn sâu hơn”
- “Một góc nhìn thực tế”
- “Phần này sẽ giúp bạn hiểu rõ”

Rewrite them to name the actual technical scope.

## Boundary test

A new heading is justified when the reader's active technical question, object or mechanism changes enough that a boundary improves navigation.

Do not create many tiny headings merely to make prose scannable.

Conversely, do not keep several unrelated mechanisms under one vague heading.
